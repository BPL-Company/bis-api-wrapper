from bis import Client

# client = Client('adsfghjyreLmkmnlgo93', 'https://bpl-id-system.herokuapp.com/')
client = Client('koza', 'http://127.0.0.1:5000/')

nick = 'Vezono4'
print()
print(client.get_user_by_id(client.get_user_by_nickname('Vezono2').id))
