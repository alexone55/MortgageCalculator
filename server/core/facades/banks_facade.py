from core.entity.banks_entity import BankEntity
from core.dao import save_model, delete_by_id, bank_dao


def get_all_banks():
    banks = BankEntity.query.all()
    output = banks_to_json(banks)

    return output


def update_bank(post_data, bank_id):
    bank_dao.update_bank(post_data, bank_id)


def banks_to_json(banks):
    output = []

    for bank in banks:
        curr_bank = {'id': bank.id,
                     'bank_name': bank.bank_name,
                     'interest_rate': bank.interest_rate,
                     'maximum_loan': bank.maximum_loan,
                     'minimum_down_payment': bank.minimum_down_payment,
                     'loan_term': bank.loan_term}
        output.append(curr_bank)

    return output


def map_and_save_bank(post_data):
    bank = BankEntity(bank_name=post_data['bank_name'],
                      interest_rate=post_data['interest_rate'],
                      maximum_loan=post_data['maximum_loan'],
                      minimum_down_payment=post_data['minimum_down_payment'],
                      loan_term=post_data['loan_term'])
    save_model(bank)


def delete_bank_func(bank_id):
    delete_by_id(BankEntity, bank_id)