# Blinkea Website

A Django-based website for Blinkea, featuring a modern UI with Tailwind CSS.

## Development Setup

1. Create a virtual environment and activate it:
```bash
python -m venv env
source env/bin/activate  # On Unix or MacOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following variables:
```
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## Deployment

This project is configured for deployment to Google Cloud Run. The deployment is automated through GitHub Actions.

### Required GitHub Secrets

Set up the following secrets in your GitHub repository:

- `GCP_PROJECT_ID`: Your Google Cloud Project ID
- `GCP_SA_KEY`: Your Google Cloud Service Account key (JSON)

### Manual Deployment

1. Build the Docker image:
```bash
docker build -t gcr.io/[PROJECT_ID]/blinkea-web .
```

2. Push to Google Container Registry:
```bash
docker push gcr.io/[PROJECT_ID]/blinkea-web
```

3. Deploy to Cloud Run:
```bash
gcloud run deploy blinkea-web --image gcr.io/[PROJECT_ID]/blinkea-web --platform managed
```
