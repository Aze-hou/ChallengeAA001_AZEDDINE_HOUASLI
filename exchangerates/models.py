from peewee import Model, CharField, CompositeKey, DateField, DecimalField
from playhouse.pool import PooledPostgresqlExtDatabase

db = PooledPostgresqlExtDatabase('exchangerates', max_connections=32, stale_timeout=300)


class ExchangeRates(Model):
    source = CharField(choices=(('ecb', 'European Central Bank'),))
    date = DateField(index=True)
    currency = CharField()
    rate = DecimalField(max_digits=16, decimal_places=6)

    class Meta:
        database = db
        primary_key = CompositeKey('date', 'currency')
