from django.shortcuts import render
from django.http import HttpResponseServerError

def error_503(request, exception=None):
    return HttpResponseServerError(render(request, '503.html'), status=503)


def home(request):
    context = {
        'features': [
            {
                'title': 'Innovative Solutions',
                'description': 'Cutting-edge technology solutions tailored to your business needs',
                'icon': 'lightbulb'
            },
            {
                'title': 'Expert Team',
                'description': 'Dedicated professionals with years of industry experience',
                'icon': 'users'
            },
            {
                'title': '24/7 Support',
                'description': 'Round-the-clock technical support and maintenance',
                'icon': 'phone'
            }
        ],
        'stats': [
            {'number': '95%', 'label': 'Client Satisfaction'},
            {'number': '500+', 'label': 'Projects Completed'},
            {'number': '50+', 'label': 'Expert Team Members'}
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
