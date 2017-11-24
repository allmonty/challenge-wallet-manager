from decimal import Decimal

from api.models import CreditCard, Wallet

class Wallet_Manager():

    def calculate_available_credit(wallet):
        available_credit = 0
        credit_cards = CreditCard.objects.filter(wallet=wallet)
        for credit_card in credit_cards:
            available_credit += credit_card.available_amount
        return available_credit

    def calculate_maximum_limit(wallet):
        maximum_limit = 0
        credit_cards = CreditCard.objects.filter(wallet=wallet)
        for credit_card in credit_cards:
            maximum_limit += credit_card.limit
        return maximum_limit
