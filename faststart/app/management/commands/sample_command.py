from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    help = 'Sample command'

    def handle_noargs(self, **options):
        verbosity = int(options.get('verbosity', 1))

        if verbosity:
            print 'This is sample command'

        #do something

        if verbosity:
            print 'All done!'
