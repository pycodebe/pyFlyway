from wrapper import Flyway

client = Flyway(verbose=False, conf_path="conf.yml")
client.help()
client.info()
client.migrate()
