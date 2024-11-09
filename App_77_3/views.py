from django.shortcuts import render

def personal_details(request):
    personal_info = {
        'name': 'T. Gopala Krishna',
        'age': 19,
        'education': [
            'BACHELOR OF TECHNOLOGY IN COMPUTER SCIENCE',
            'I HAVE ACHIEVED SO MANY MEDALS IN SCHOOL AND IN MY +12 CLASS .'
        ],
        'address': 'SRINAGAR COLONY',
        'blood_group': 'O POSITIVE',
        'hobbies': [
            'READING BOOKS',
            'WATCHING MOVIES',
            'PLAYING CRICKET',
            'TRAVELLING',
            'EXPLORING NEW THINGS'
        ],
        'skills': [
            'PYTHON',
            'DJANGO',
            'HTML',
            'CSS',
            'JAVASCRIPT'
        ],
        'interests': [
            'WEB DEVELOPMENT',
            'MACHINE LEARNING',
            'DATA SCIENCE'
        ],            
        'languages_known': ['English', 'Telugu', 'Hindi'],
        'contact_info': {
            'email': 'krishna@gmail.com',
            'phone': '+91 9876543210'
        },
        'about_me': 'I am a passionate learner with a keen interest in technology and innovation. I enjoy solving problems and working on projects that challenge my skills and creativity.'
    }
    
    return render(request, 'personal_details.html', personal_info)



def portfolio(request):
    projects = [
        {
            'title': 'Project 1',
            'description': 'Developed a website of Disaster management.',
        },
        {
            'title': 'Project 2',
            'description': 'Developed a portfolio for personal information.',
        },
        # Add more projects as needed
    ]
    achievements = [
        {
            'title': 'Achievement 1',
            'description': 'Achieved 2nd prize in Robo race conducted by the college.',
        },
        {
            'title': 'Achievement 2',
            'description': 'Achieved 1st prize in a Cricket match conducted by the college.',
        },
        # Add more achievements as needed
    ]
    social_media={
        'github': 'https://github.com/Krishna28-del',
        },
        
    
    return render(request, 'portfolio.html', {'projects': projects, 'achievements': achievements,'social_media': social_media})