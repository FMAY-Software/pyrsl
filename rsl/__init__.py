# encoding: utf-8
# Copyright (C) 2015 John Törnblom
'''
Parsing and evaluation of the rule-specification language (RSL).  
'''
from rsl.parse import parse_file
from rsl.parse import parse_text
from rsl.eval import evaluate
from rsl.runtime import Runtime
from rsl.runtime import bridge
from rsl.gen_erate import main
