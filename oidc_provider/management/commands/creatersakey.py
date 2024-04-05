from Cryptodome.PublicKey import RSA
from django.core.management.base import BaseCommand
from oidc_provider.models import RSAKey
from oidc_provider import settings


encrypt = settings.import_hook('OIDC_RSA_ENCRYPT_HOOK')
decrypt = settings.import_hook('OIDC_RSA_DECRYPT_HOOK')


class Command(BaseCommand):
    help = 'Randomly generate a new RSA key for the OpenID server'

    def add_arguments(self, parser):
        if encrypt is None:
            return

        parser.add_argument(
            '--encrypted',
            '-e',
            action='store_true',
            help='Encrypt key',
        )

    def handle(self, *_, **options):
        key = RSA.generate(2048)
        rsakey = RSAKey(
            key=key.exportKey('PEM').decode('utf8'),
            encrypted=options.get('encrypted', False),
        )
        rsakey.save()
        self.stdout.write(u'RSA key successfully created with kid: {0}'.format(rsakey.kid))
