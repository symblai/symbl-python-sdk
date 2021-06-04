import unittest
from unittest.mock import Mock, patch

import symbl_rest
from symbl import AuthenticationToken
from symbl_rest import Configuration, ApiClient

from types import SimpleNamespace


class AuthenticationTokenTest(unittest.TestCase):

    def test_get_access_token_should_succeed_given_valid_token(self):
        demo_response = SimpleNamespace(**{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFVUTRNemhDUVVWQk1rTkJNemszUTBNMlFVVTRRekkyUmpWQ056VTJRelUxUTBVeE5EZzFNUSJ9.eyJodHRwczovL3BsYXRmb3JtLnN5bWJsLmFpL3VzZXJJZCI6IjYyOTg2MTI4NTIwNjQyNTYiLCJpc3MiOiJodHRwczovL2RpcmVjdC1wbGF0Zm9ybS5hdXRoMC5jb20vIiwic3ViIjoiWGNaYnA2MVk1dHJRVWEzVXhOZzkxc3MwSzdXRHN4UVdAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vcGxhdGZvcm0ucmFtbWVyLmFpIiwiaWF0IjoxNjIyODA5NzU4LCJleHAiOjE2MjI4OTYxNTgsImF6cCI6IlhjWmJwNjFZNXRyUVVhM1V4Tmc5MXNzMEs3V0RzeFFXIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.IXdme9NTdaiQFEUIgyfUtKPa8SYMXahcJ8mYRVi5gER4ntqqxeMoSBuIiZJNzwfOfsxZ-HO--azKsGokqJWtuZ3BMeW2OpucFyV1TGbbcYcXWrZwPSlMmcsfXMUlXGxCf7dnfmM48pUNTnpmS6jKpGyAPK4TCaHutSva0wWK93laB2c-ueM7UZ03u-onMkPMykg7_QqStx82ogaanSX-XUHNI7SuODy8strTIpW2DKzOgvg9S6PzDC3zvDyD-sdfXtYsByn8R94CxcGQ9kUs8AF_hOlwUdp_Apq2U57naoXPd3aQx4rRtPl52_2GU6CeGAK7IgI26WWCgcHAe3mLow","expires_in":76254})
        string_value = "demo_value"
        with patch("symbl_rest.AuthenticationApi.generate_token", Mock(return_value=demo_response)), patch("configparser.ConfigParser.get", Mock(return_value=string_value)):
            self.assertEqual(demo_response.access_token, AuthenticationToken.get_access_token())

    def test_get_api_header_should_succeed_given_valid_token(self):
        demo_response = SimpleNamespace(**{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFVUTRNemhDUVVWQk1rTkJNemszUTBNMlFVVTRRekkyUmpWQ056VTJRelUxUTBVeE5EZzFNUSJ9.eyJodHRwczovL3BsYXRmb3JtLnN5bWJsLmFpL3VzZXJJZCI6IjYyOTg2MTI4NTIwNjQyNTYiLCJpc3MiOiJodHRwczovL2RpcmVjdC1wbGF0Zm9ybS5hdXRoMC5jb20vIiwic3ViIjoiWGNaYnA2MVk1dHJRVWEzVXhOZzkxc3MwSzdXRHN4UVdAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vcGxhdGZvcm0ucmFtbWVyLmFpIiwiaWF0IjoxNjIyODA5NzU4LCJleHAiOjE2MjI4OTYxNTgsImF6cCI6IlhjWmJwNjFZNXRyUVVhM1V4Tmc5MXNzMEs3V0RzeFFXIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.IXdme9NTdaiQFEUIgyfUtKPa8SYMXahcJ8mYRVi5gER4ntqqxeMoSBuIiZJNzwfOfsxZ-HO--azKsGokqJWtuZ3BMeW2OpucFyV1TGbbcYcXWrZwPSlMmcsfXMUlXGxCf7dnfmM48pUNTnpmS6jKpGyAPK4TCaHutSva0wWK93laB2c-ueM7UZ03u-onMkPMykg7_QqStx82ogaanSX-XUHNI7SuODy8strTIpW2DKzOgvg9S6PzDC3zvDyD-sdfXtYsByn8R94CxcGQ9kUs8AF_hOlwUdp_Apq2U57naoXPd3aQx4rRtPl52_2GU6CeGAK7IgI26WWCgcHAe3mLow","expires_in":76254})
        string_value = "demo_value"
        with patch("symbl_rest.AuthenticationApi.generate_token", Mock(return_value=demo_response)), patch("configparser.ConfigParser.get", Mock(return_value=string_value)):
            self.assertEqual({'x-api-key': demo_response.access_token}, AuthenticationToken.get_api_header())

    def test_get_api_client_should_succeed_given_valid_token(self):
        demo_response = SimpleNamespace(**{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFVUTRNemhDUVVWQk1rTkJNemszUTBNMlFVVTRRekkyUmpWQ056VTJRelUxUTBVeE5EZzFNUSJ9.eyJodHRwczovL3BsYXRmb3JtLnN5bWJsLmFpL3VzZXJJZCI6IjYyOTg2MTI4NTIwNjQyNTYiLCJpc3MiOiJodHRwczovL2RpcmVjdC1wbGF0Zm9ybS5hdXRoMC5jb20vIiwic3ViIjoiWGNaYnA2MVk1dHJRVWEzVXhOZzkxc3MwSzdXRHN4UVdAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vcGxhdGZvcm0ucmFtbWVyLmFpIiwiaWF0IjoxNjIyODA5NzU4LCJleHAiOjE2MjI4OTYxNTgsImF6cCI6IlhjWmJwNjFZNXRyUVVhM1V4Tmc5MXNzMEs3V0RzeFFXIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.IXdme9NTdaiQFEUIgyfUtKPa8SYMXahcJ8mYRVi5gER4ntqqxeMoSBuIiZJNzwfOfsxZ-HO--azKsGokqJWtuZ3BMeW2OpucFyV1TGbbcYcXWrZwPSlMmcsfXMUlXGxCf7dnfmM48pUNTnpmS6jKpGyAPK4TCaHutSva0wWK93laB2c-ueM7UZ03u-onMkPMykg7_QqStx82ogaanSX-XUHNI7SuODy8strTIpW2DKzOgvg9S6PzDC3zvDyD-sdfXtYsByn8R94CxcGQ9kUs8AF_hOlwUdp_Apq2U57naoXPd3aQx4rRtPl52_2GU6CeGAK7IgI26WWCgcHAe3mLow","expires_in":76254})
        string_value = "demo_value"
        configuration_instance = Configuration()
        configuration_instance.api_key['x-api-key'] = demo_response.access_token
        with patch("symbl_rest.AuthenticationApi.generate_token", Mock(return_value=demo_response)), patch("configparser.ConfigParser.get", Mock(return_value=string_value)):
            returnValue = AuthenticationToken.get_api_client()
            self.assertIsNotNone(returnValue)
            self.assertIsInstance(returnValue, symbl_rest.ApiClient)
            self.assertEqual(returnValue.configuration.api_key, configuration_instance.api_key)

if __name__ == '__main__':
    unittest.main()
