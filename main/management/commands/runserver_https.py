from django.core.management.commands.runserver import Command as RunserverCommand
from django.conf import settings
import os

class Command(RunserverCommand):
    help = 'Runs the server with HTTPS support'

    def handle(self, *args, **options):
        # Check if SSL certificate and key exist
        if not os.path.exists(settings.SSL_CERTIFICATE) or not os.path.exists(settings.SSL_PRIVATE_KEY):
            self.stderr.write(self.style.ERROR(
                'SSL certificate or key not found. Please generate them first:\n'
                'mkdir -p certs && cd certs && openssl req -x509 -nodes -days 365 -newkey rsa:2048 '
                '-keyout localhost.key -out localhost.crt -subj "/C=US/ST=CA/L=San Francisco/O=Development/CN=localhost"'
            ))
            return

        # Add SSL certificate options
        options['cert_path'] = settings.SSL_CERTIFICATE
        options['key_path'] = settings.SSL_PRIVATE_KEY
        options['ssl_version'] = 2  # Use TLS

        super().handle(*args, **options)
