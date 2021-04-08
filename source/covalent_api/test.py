# # :coding: utf-8
# # :copyright: Copyright (c) 2021 Lluis Casals Marsol
# # Copyright 2021 Lluis Casals Marsol.
# # All rights reserved.
# # Please see the LICENSE file that should have been included as part of this
# # package.
#
#
# from covalent_api import constants
# from covalent_api import url_utils
#
# # Todo we can have an schema of this kind so define all the functions and
# #  arguments and with the test function execute what is needed.
# function_map = {
#     'Get log events by contract adress': {
#         'path_parameters': {
#             'chain_id':{
#                 'type':'enum',
#                 'items':[1,137],
#                 'mandatory':true
#             },
#             'address':{
#                 'type':'string',
#                 'mandatory':true
#             }
#         }
#         'query_parameters':{
#             'string-block':{'mandatory':true},
#             'ending-block':{'mandatory':true},
#             'page-number':{'mandatory':false},
#             'page-size':{'mandatory':false},
#             'format'={'mandatory':false}
#         },
#         'query_path':'events',
#         'path_order':['chain_id',query_path, address]
#     }
# }
#
#
# class ClassA(object):
#
#     @property
#     def base_url(self):
#         return self._base_url
#
#     @property
#     def session(self):
#         return self._session
#
#     def __init__(self, session):
#         self._base_url = "pricing/"
#         self._session = session
#
#     def test_funcition(self, function_name, **kwargs):
#         #Call this function get_logs_events_by_topic_hash(**dictionary)
#         if function_name not in constants.functions:
#             return
#         funtion_maping = constants.funtion(function_name)
#         funtion_maping = {
#                              get_token_balances_for_address: chain_id, address, nft=None, no_nft_fetch=None, format="json"}
#
#     def get_token_balances_for_address(
#             self, chain_id, address, nft=None, no_nft_fetch=None, format="json"
#     ):
#         # TODO: on the api docs says the following for the address argument:
#         #  Passing in an ENS resolves automatically. But I don't know what an
#         #  ENS is.
#         if chain_id not in constants.AVAILABLE_CHAIN_IDS:
#             raise Exception(
#                 "chain_id should be one of {}".format(
#                     list(constants.AVAILABLE_CHAIN_IDS.values)
#                 )
#             )
#
#         method_url = "balances_v2"
#         address = "address/" + address
#         url_args = [chain_id, address, method_url]
#
#         url = url_utils.generate_url(self.base_url, url_args)
#         params = {
#             'nft': nft,
#             'no-nft-fetch': no_nft_fetch,
#             'format': format
#         }
#         decode = format == 'json'
#
#         result = self.session.query(url, params, decode=decode)
#         return result
#
#     def get_historical_portfolio_value_over_time(
#             self, chain_id, address, quote_currency=None, format="json"
#     ):
#         # TODO: same as get_token_balances_for_address
#         if chain_id not in constants.AVAILABLE_CHAIN_IDS:
#             raise Exception(
#                 "chain_id should be one of {}".format(
#                     list(constants.AVAILABLE_CHAIN_IDS.values)
#                 )
#             )
#
#         method_url = "portfolio_v2"
#         address = "address/" + address
#         url_args = [chain_id, address, method_url]
#
#         url = url_utils.generate_url(self.base_url, url_args)
#         params = {
#             'quote-currency': quote_currency,
#             'format': format
#         }
#         decode = format == 'json'
#
#         result = self.session.query(url, params, decode=decode)
#         return result
#
#     def get_transactions(
#             self, chain_id, address, block_signed_at_asc=None, no_logs=None,
#             page_number=None, page_size=None, format="json"
#     ):
#         # TODO: same as get_token_balances_for_address
#         if chain_id not in constants.AVAILABLE_CHAIN_IDS:
#             raise Exception(
#                 "chain_id should be one of {}".format(
#                     list(constants.AVAILABLE_CHAIN_IDS.values)
#                 )
#             )
#
#         method_url = "transactions_v2"
#         address = "address/" + address
#         url_args = [chain_id, address, method_url]
#
#         url = url_utils.generate_url(self.base_url, url_args)
#         params = {
#             'block-signed-at-asc': block_signed_at_asc,
#             'no-logs': no_logs,
#             'page-number': page_number,
#             'page-size': page_size,
#             'format': format
#         }
#         decode = format == 'json'
#
#         result = self.session.query(url, params, decode=decode)
#         return result
#
#     def get_block(
#             self, chain_id, block_height, format="json"
#     ):
#
#         if chain_id not in constants.AVAILABLE_CHAIN_IDS:
#             raise Exception(
#                 "chain_id should be one of {}".format(
#                     list(constants.AVAILABLE_CHAIN_IDS.values)
#                 )
#             )
#
#         method_url = "block_v2"
#         url_args = [chain_id, method_url, block_height]
#
#         url = url_utils.generate_url(self.base_url, url_args)
#         params = {
#             'format': format
#         }
#         decode = format == 'json'
#
#         result = self.session.query(url, params, decode=decode)
#         return result
#
#     def get_log_events_by_contract_address(
#             self, chain_id, address, starting_block, ending_block,
#             page_number=None, page_size=None, format="json"
#     ):
#         # TODO: same as get_token_balances_for_address
#         if chain_id not in constants.AVAILABLE_CHAIN_IDS:
#             raise Exception(
#                 "chain_id should be one of {}".format(
#                     list(constants.AVAILABLE_CHAIN_IDS.values)
#                 )
#             )
#
#         method_url = "events"
#         address = "address/" + address
#         url_args = [chain_id, method_url, address]
#
#         url = url_utils.generate_url(self.base_url, url_args)
#         params = {
#             'starting-block': starting_block,
#             'ending-block': ending_block,
#             'page-number': page_number,
#             'page-size': page_size,
#             'format': format
#         }
#         decode = format == 'json'
#
#         result = self.session.query(url, params, decode=decode)
#         return result
#
#
#
