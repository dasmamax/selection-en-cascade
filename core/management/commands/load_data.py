from django.core.management.base import BaseCommand
from core.models import Course, Module

class Command(BaseCommand):
    help = 'Load Courses and Modules'

    def handle(self, *args, **kwargs):
        Module.objects.all().delete()
        course_names = [
            'Anglais', 'Francais', 'Allemand', 'Ashanto'
        ]

        if not Course.objects.count():
            for course_name in course_names:
                Course.objects.create(name=course_name)

        # Computer Science
        cs = Course.objects.get(name='Anglais')

        compsci_modules = [
            'I',
            'You',
            'He/She',
            'We', 
            
        ]

        for module in compsci_modules:
            Module.objects.create(name=module, course=cs)

        # Maths
        math = Course.objects.get(name='Francais')
        math_modules = [
            'Je',
            'Tu',
            'Il',
            'Nous',
            'Vous'
        ]

        for module in math_modules:
            Module.objects.create(name=module, course=math)

        # PHYSICS
        physics = Course.objects.get(name='Allemand')
        physics_modules = [
            'Ich',
            'Du',
            'Er',
            'Wir',
            'Ihr'
        ] 
        for module in physics_modules:
            Module.objects.create(name=module, course=physics)

        # Film
        film = Course.objects.get(name='Ashanto')

        film_modules = [
            'I',
            'Fu',
            'Ou',
            'Ti',
            'Ni'
        ]

        for module in film_modules:
            Module.objects.create(name=module, course=film)