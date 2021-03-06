# encoding: utf-8

# This example deletes one or more Historics queries in your account.

import sys, os
from datetime import datetime
sys.path[0:0] = [os.path.join(os.path.dirname(__file__), "..", ".."),]
import datasift
from env import Env

# Set up the environment
env = Env(sys.argv)

# Make sure we have something to do
if env.get_arg_count() == 0:
    sys.stderr.write('Please specify one or more playback IDs\n')
    sys.exit(1)

try:
    # Go through the playback_ids we've been given
    for playback_id in env.get_args():
        # Get the Historics query
        historic = env.get_user().get_historic(playback_id)

        # Delete it
        print 'Deleting %s...' % (playback_id)
        historic.delete()
except datasift.InvalidDataError, e:
    sys.stderr.write('InvalidDataError: %s\n' % e)
except datasift.APIError, e:
    sys.stderr.write('APIError: %s\n' % e)
except datasift.AccessDeniedError, e:
    sys.stderr.write('InvalidDataError: %s\n' % e)

sys.stderr.write('Rate-limit-remaining: %s\n' % str(env.get_user().get_rate_limit_remaining()));
