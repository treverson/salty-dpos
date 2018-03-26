import re
import sys
import math
import json
import requests
import os.path

class dposAPI(object):

    def __init__(self,rturl=''):

        self.headers = {'content-type': 'application/json'}
        self.target_url = rturl

    def requests_check(self, url, req_type, payload=None):
        """
        """

        resp = {'success': True}

        try:

            if req_type == 'GET':

                r = requests.get(url)

            elif req_type == 'PUT':

                if not payload:
                    resp['success'] = False
                else:
                    r = requests.put(url, json=payload,
                                     headers=self.headers)

            elif req_type == 'POST':

                if not payload:
                    resp['success'] = False
                else:
                    r = requests.post(url, json=payload,
                                      headers=self.headers)

                if r.status_code != 200:

                    raise ValueError('A very specific bad thing happened')

            resp = r.json()

        except ValueError as error:

            resp['success'] = False
            resp['message'] = str(error)

        except Exception as err:

            resp['success'] = False
            resp['message'] = "{}".format(err)


        return resp

    def loader(self, rtype):

        targets = {
                # Will return account's delegates by address.
                # GET /api/loader/status
                'status' : '/api/loader/status',
                # Get synchronization status of wallet.
                # GET /api/loader/status/sync
                'sync' : '/api/loader/status/sync',
            }

        url = self.target_url + targets[rtype]

        return  self.requests_check(url, 'GET')

    def account(self,rtype,payload={}):

        targets = {
                # Open account in wallet.
                # POST /api/accounts/open
                'open_account' : '/api/accounts/open',
                # Get balance of account.
                # GET /api/accounts/getBalance?address=address
                'balance' : '/api/accounts/getBalance?address=',
                # Get public key of account. 
                # GET /api/accounts/getPublicKey?address=address
                'pubkey' : '/api/accounts/getPublicKey?address=',
                # Will return public key of provided secret key.
                # POST /api/accounts/generatePublicKey
                'genpub' : '/api/accounts/generatePublicKey',
                # Will return account by address.
                # GET /api/accounts?address=address
                'account' : '/api/accounts?address=',
                # Will return account's delegates by address.
                # GET /api/accounts/delegates?address=address 
                'delegates_by_account' : '/api/accounts/delegates?address=',
                # Will vote for selected delegates.
                # PUT /api/accounts/delegates
                'vote' : '/api/accounts/delegates',
            }

        req_methods = {
                'get' : ['balance','account','pubkey','delegates_by_account'],
                'put' : ['vote'],
                'post' : ['genpub','open_account']
            }

        url = self.target_url + targets[rtype]

        if rtype in req_methods['get']:

            if not payload.get('address'):

                return {'success': False, 'error': 'No address given'}

            else:

                url = self.target_url + targets[rtype] + payload['address']

                return self.requests_check(url, 'GET')

        elif rtype in req_methods['put']:

            return self.requests_check(url, 'PUT', payload)

        elif rtype in req_methods['post']:

            return self.requests_check(url, 'POST', payload)

        else:

            return {'success': False, 'error': 'Option not recognized'}



    def transactions(self,rtype,payload={}):

        targets = {
                # Transactions list matched by provided parameters.
                # GET /api/transactions?blockId=blockId&senderId=senderId&
                # recipientId=recipientId&limit=limit&offset=offset&orderBy=field
                'blocktx' : '/api/transactions',
                # Send transaction to broadcast network.
                # PUT /api/transactions
                'send' : '/api/transactions',
                # Transaction matched by id.
                # GET /api/transactions/get?id=id
                'get_tx' : '/api/transactions/get?id=',
                # Get unconfirmed transaction by id.
                # GET /api/transactions/unconfirmed/get?id=
                'unconfirmed' : '/api/transactions/unconfirmed/get?id=',
                # Get list of unconfirmed transactions.
                # GET /api/transactions/unconfirmed
                'unconfirmed_all' : '/api/transactions/unconfirmed',
                # Gets a list of queued transactions.
                # GET /api/transactions/queued
                'queued_all': '/api/transactions/queued',
                # Get queued transaction that matches the provided id.
                # GET /api/transactions/queued/get?id=id
                'queued': '/api/transactions/queued/get?id=',
                # get all multisig
                'multisignature_all': '/api/transactions/multisignatures',
                # get one multisig
                'multisignature': '/api/transactions/multisignatures/get?id='
            }


        req_methods = {
               'get' : ['blocktx','get_tx','unconfirmed','unconfirmed_all',
                        'queued', 'queued_all', 'multisignature_all',
                        'multisignature'],
               'put' : ['send']
            }

        url = self.target_url + targets[rtype]

        if rtype in req_methods['get']:

            if payload['id'] and not payload['parameters']:

                url += payload['id']

            elif payload['parameters'] and not payload['id']:

                url += payload['parameters']

            elif rtype == 'multisignature_all':

                url = '{}{}'.format(self.target_url, targets[rtype])

            elif rtype == 'multisignature':

                try:

                    url = '{}{}{}'.format(self.target_url, targets[rtype],
                                          payload['id'])
                except KeyError:

                    return "No id provided with multisignature"


            else:

                if rtype == 'queued' and not payload['parameters']:

                    return "unconfirmed option requires a -p parameter"

                else:

                    url = url

            return self.requests_check(url, 'GET')

        elif rtype in req_methods['put']:

            return self.requests_check(url, 'PUT', payload)

        else:

            return "Option Not Recognized"


    def peers(self,rtype,payload={}):

        targets = {
                # Get peers list by parameters.
                # GET /api/peers?state=state&os=os&shared=shared&
                # version=version&limit=limit&offset=offset&orderBy=orderBy
                'peer_list' : '/api/peers',
                # Get peer by ip and port
                # GET /api/peers/get?ip=ip&port=port
                'peer_ip' : '/api/peers/get?ip="{}"&port={}'.\
                    format(payload['ip'], payload['port']),
                # Get peer version and build time
                # GET /api/peers/version
                'peer_version' : '/api/peers/version',
            }


        url = '{}{}'.format(self.target_url, targets[rtype])

        if payload['parameters']:

             url = '{}{}'.format(url, payload['parameters'])

        return self.requests_check(url, 'GET')


    def blocks(self,rtype,payload={}):

        targets = {
                # Get block by id.
                # GET /api/blocks/get?id=id
                'blockid' : '/api/blocks/get?id=',
                # Get all blocks.
                # GET /api/blocks?generatorPublicKey=generatorPublicKey
                # &height=height&previousBlock=previousBlock&totalAmount=totalAmount
                # &totalFee=totalFee&limit=limit&offset=offset&orderBy=orderBy
                'all_blocks' : '/api/blocks',
                # Get blockchain fee percent
                # GET /api/blocks/getFee
                'fee' : '/api/blocks/getFee',
                # Get blockchain height
                # GET /api/blocks/getHeight
                'height' : '/api/blocks/getHeight',
                #
                'my_blocks' : '/api/blocks?generatorPublicKey=',
            }

        get = ['my_blocks','blockid','all_blocks','fee','height']

        url = self.target_url + targets[rtype]

        if rtype in get:

            if rtype == 'blockid' or rtype == 'all_blocks':

                url += payload['parameters']

            elif rtype == 'my_blocks':

                url += payload['pubkey']

        return self.requests_check(url, 'GET')


    def signatures(self, rtype, payload={}):

	targets = {

            # Get second signature of account.
            # GET /api/signatures/get?id=id
            'get_signature' : '/api/signatures/get?id=',

            # Add second signature to account.
            # PUT /api/signatures
            'gen_2_sig' : '/api/signatures',

        }

        request_method = {
                'get' : ['get_signature'],
                'put' : ['gen_2_sig']
            }

        url = self.target_url + targets[rtype]

        if rtype in request_method['get']:

            url = self.target_url + targets[rtype] + payload['id']

            return self.requests_check(url, 'GET')

        elif rtype in request_method['put']:

            return self.put_check(url, 'PUT', payload)

    def delegates(self, rtype, payload={}):

        targets = {

                # Enable delegate on account
                # PUT /api/delegates
                'register_delegate' : '/api/delegates',

                # Get delegates list.
                # GET /api/delegates?limit=limit&offset=offset&orderBy=orderBy
                'delegate_list' : '/api/delegates',

                # Get delegate by transaction id.
                # GET /api/delegates/get?id=transactionId
                'delegate_by_tx' : '/api/delegates/get?id=',

                # Get votes by account address.
                # GET /api/accounts/delegates/?address=address
                'votes_by_account' : '/api/accounts/delegates/?address=',

                # Enable forging
                # POST /api/delegates/forging/enable
                'enable_forging' : '/api/delegates/forging/enable',

                # Disable forging
                # POST /api/delegates/forging/disable
                'disable_forging' : '/api/delegates/forging/disable',

                # Get voters of delegate.
                # GET /api/delegates/voters?publicKey=publicKey
                'delegate_voters' : '/api/delegates/voters?publicKey=',

                # Get forged by account
                # Get amount forged by account.
                'forged' : '/api/delegates/forging/getForgedByAccount?generatorPublicKey=',

                # Get next forging delegates
                'next_forgers': '/api/delegates/getNextForgers'
            }

        request_method = {
                'get' : ['delegate_list','delegate_by_tx','votes_by_account',
                    'forged','delegate_voters', 'next_forgers'],
                'put' : ['register_delegate'],
                'post' : ['enable_forging','disable_forging']
                }

        url = self.target_url + targets[rtype]

        if rtype in request_method['get']:

            if rtype == 'delegate_by_tx':

                url += payload['id']

            elif rtype == 'votes_by_account':

                url += payload['address']

            elif rtype == 'delegate_voters' or rtype in 'forged':

                url += payload['pubkey']

            elif rtype == 'delegate_list':

                url += payload['parameters']

            return self.requests_check(url, 'GET')

        elif rtype in request_method['put']:

            if 'secret' in payload and 'username' in payload:

                return self.requests_check(url, 'PUT', payload)

            else:

                error = {'dposAPI': 'Dictionary does not contain required items'}
                return error

        elif rtype in request_method['post']:

            return self.requests_check(url, 'POST', payload)

    def usernames(self,rtype,payload):

        targets = {
                # Register username.
                # PUT /api/accounts/username
                'register_username' : '/api/accounts/username'
            }

        url = self.target_url + targets[rtype]

        return self.put_check(url,payload,self.headers)

    def contacts(self,rtype,payload):

        targets = {
                # Add contact
                # PUT /api/contacts
                'add_contact' : '/api/contacts',
                # Get contacts of account by public key.
                # GET /api/contacts/?publicKey=publicKey
                'contacts' : '/api/contacts/?publicKey=',
                # Get unconfirmed contacts of account by public key.
                # /api/contacts/unconfirmed?publicKey=publicKey
                'unconfirmed_contacts' : '/api/contacts/unconfirmed?publicKey='
            }

        request_method = {
                'get' : ['contacts','unconfirmed_contacts'],
                'put' : ['add_contact']
            }

        if rtype in request_method['get']:

            url = '{}{}{}'.format(self.target_url,targets[rtype],payload['pubkey'])

            return self.get_check(url)

        elif rtype in request_method['put']:

            url = '{}{}'.format(self.target_url,targets[rtype])

            return self.put_check(url,payload,self.headers)


    # Custom Wrappers
    def autoname(self, delegate):
        '''
        Give a username get account information
        '''

        payload = {'parameters': '/get?username={}'.format(delegate)}
        delegate_info = self.delegates('delegate_list', payload)

        return delegate_info

    def my_voters(self,wallet):

        ## Get my voters
        account_payload = { 'address' : wallet }
        voters_payload = {}

        ## Get the public key
        pkey = self.account('pubkey',account_payload)

        voters_payload['pubkey'] = pkey['publicKey']

        ## Get your voters
        voters = self.delegates('delegate_voters',voters_payload)

        return voters

    def forge_check(self, delegate):
        ''' check forging status '''

        # First grab public key from delegate name
        payload = {'parameters':'/get?username={}'.format(delegate)}
        delegate_info = self.delegates('delegate_list',payload)

        if delegate_info.get('success') is False:

            return {'enabled': False, 'err': delegate_info}

        pubkey = delegate_info['delegate']['publicKey']

        response = requests.get('{}/api/delegates/forging/status?publicKey={}'\
                                .format(self.target_url, pubkey))

        return json.loads(response.text)


    def get_network_height(self, nethash, port, version):
        '''
        Get the height of the network
        '''

        data = {
            'version' : '{}'.format(version),
            'Accept': '*/*',
            'Connection': 'close',
            'os': 'linux3.13.0-85-generic',
            'port': '{}'.format(port),
            'accept': 'application/json',
            'User-Agent': 'https://github.com/blakeembrey/popsicle',
            'Accept-Encoding': 'gzip, deflate',
            'nethash': nethash
        }

        height_list = []

        # Get the peer list from login dpos io
        peer_list = '{}/peer/list'.format(self.target_url)

        #
        peer_height = 'http://{}:{}/peer/height'

        try:
            resp = self.requests_check(peer_list, 'GET')
        except ValueError:
            pass

        for peer in resp['peers']:

            try:
                res = requests.get(peer_height.format(peer['ip'], port),
                                   headers=data,  timeout=0.3).json()
                height_list.append(res['height'])
            except requests.exceptions.ConnectionError:
                pass
            except requests.exceptions.Timeout:
                pass
            except KeyError:
                pass
            except ValueError:
                pass

        if height_list:
            return max(height_list)
        else:
            return 0
