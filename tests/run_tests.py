#!/usr/bin/env python
import unittest, os, glob

# Import the tests
from test_user        import TestUser
from test_definition  import TestDefinition
from test_push        import TestPush

# Run the tests
log_file = "build.log"
f = open(log_file, "w")
runner = unittest.TextTestRunner(f)
unittest.main(testRunner=runner)
