# Local Development Configuration
# Import and override the main config for local development

from config import SITE_CONFIG

# Create a copy for local development
LOCAL_CONFIG = SITE_CONFIG.copy()

# Override baseurl for local development
LOCAL_CONFIG['baseurl'] = ''  # Empty for localhost

# You can override other settings here as needed
# LOCAL_CONFIG['output_dir'] = 'docs'
