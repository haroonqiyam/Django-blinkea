from django.shortcuts import render

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
