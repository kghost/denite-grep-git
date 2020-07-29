# -*- coding: utf-8 -*-

from denite.source.grep import Source as Grep

class Source(Grep):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'grep/git'
        self.vars.update({
            'command': ['git', '--no-pager', 'grep'],
            'default_opts': ['-n', '--no-color'],
            'recursive_opts': [],
            'pattern_opt': ['-e'],
            'separator': ['--'],
            'final_opts': [],
            'min_interactive_pattern': 3,
        })
