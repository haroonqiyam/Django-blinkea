from django.shortcuts import render
from django.http import HttpResponseServerError

def error_503(request, exception=None):
    return HttpResponseServerError(render(request, '503.html'), status=503)


def home(request):
    context = {
        'clients': [
            {'name': 'BSMI', 'logo': 'img/clients/bsmi.svg'},
            {'name': 'Cartier', 'logo': 'img/clients/cartier.svg'},
            {'name': 'ICBA', 'logo': 'img/clients/icba.svg'},
            {'name': 'Precision', 'logo': 'img/clients/precision.svg'},
            {'name': 'Berger', 'logo': 'img/clients/berger.svg'},
            {'name': 'Damilano', 'logo': 'img/clients/damilano.svg'},
        ],
        'projects': [
            {
                'title': 'DarkBox',
                'category': 'Branding Design, Product Design',
                'image': 'img/portfolio/darkbox.svg'
            },
            {
                'title': 'Eo',
                'category': 'Branding Service, Website UX/UI Design',
                'image': 'img/portfolio/eo.svg'
            },
            {
                'title': 'TaxiAI',
                'category': 'Application Analytics',
                'image': 'img/portfolio/taxiai.svg'
            },
            {
                'title': 'Eliosa',
                'category': 'Branding Service, FMCG',
                'image': 'img/portfolio/eliosa.svg'
            },
            {
                'title': 'Azeta',
                'category': 'UI Design & Branding, Product Packaging',
                'image': 'img/portfolio/azeta.svg'
            },
            {
                'title': 'Vabix',
                'category': 'Branding Service, Website Design',
                'image': 'img/portfolio/vabix.svg'
            },
            {
                'title': 'Ice & Joy',
                'category': 'Branding Service, Design & Technology',
                'image': 'img/portfolio/ice-joy.svg'
            },
            {
                'title': 'BIT',
                'category': 'UI Design & Branding, Website Design',
                'image': 'img/portfolio/bit.svg'
            },
        ]
    }
    return render(request, 'website/home.html', context)


def solutions(request):
    context = {
        'solutions': [
            {
                'title': 'Data Analytics',
                'description': 'Transform your raw data into actionable insights with our advanced analytics solutions.',
                'icon': 'chart-bar'
            },
            {
                'title': 'Machine Learning',
                'description': 'Leverage the power of AI to automate processes and make data-driven decisions.',
                'icon': 'brain'
            },
            {
                'title': 'Cloud Solutions',
                'description': 'Scale your infrastructure efficiently with our cloud-native solutions.',
                'icon': 'cloud'
            },
        ]
    }
    return render(request, 'website/solutions.html', context)
