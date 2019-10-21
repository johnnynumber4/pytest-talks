class Config:
    def __init__(self, env):
        SUPPORTED_ENVS = ['dev', 'qa']

        if env.lower() not in SUPPORTED_ENVS:
            raise Exception(f'{env} is not a supported environment.  Supported envs are {SUPPORTED_ENVS}')
        
        self.base_url = {
            'dev':'https://my-devenv.com',
            'qa':'https://my-qaenv.com',
            'staging': 'https://my-stagingenv.com'
        }[env]

        self.app_port = {
            'dev': 80,
            'qa': 8080,
            'staging': 5000
        }[env]


