from django.http import JsonResponse
from django.views import View
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class HealthCheckView(View):
    def get(self, request, *args, **kwargs):
        try:
            # Check database connection
            from django.db import connections
            db_conn = connections['default']
            db_conn.cursor()
            db_status = True
        except Exception as e:
            logger.error(f"Database connection failed: {str(e)}")
            db_status = False

        # Check Redis connection if using Celery
        redis_status = False
        if hasattr(settings, 'CELERY_BROKER_URL'):
            try:
                from redis import Redis
                redis_url = settings.CELERY_BROKER_URL
                redis_client = Redis.from_url(redis_url)
                redis_client.ping()
                redis_status = True
            except Exception as e:
                logger.error(f"Redis connection failed: {str(e)}")

        # Collect system info
        health_status = {
            "status": "healthy" if db_status else "unhealthy",
            "database": {
                "connected": db_status,
                "engine": settings.DATABASES['default']['ENGINE'],
                "name": settings.DATABASES['default']['NAME'],
                "host": settings.DATABASES['default']['HOST']
            },
            "redis": {
                "connected": redis_status,
                "url": settings.CELERY_BROKER_URL if hasattr(settings, 'CELERY_BROKER_URL') else None
            },
            "environment": "production" if not settings.DEBUG else "development",
            "allowed_hosts": settings.ALLOWED_HOSTS,
            "static_root": settings.STATIC_ROOT,
            "media_root": settings.MEDIA_ROOT,
            "port": settings.PORT
        }
        
        response = JsonResponse(health_status)
        if not db_status:
            response.status_code = 503
        return response
