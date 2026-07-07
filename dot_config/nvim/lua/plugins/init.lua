local Plug = vim.fn['plug#']

vim.call('plug#begin')

Plug('nvim-treesitter/nvim-treesitter', {['do'] = ':TSUpdate'})
Plug 'nvim-treesitter/nvim-treesitter-context'
Plug 'lukas-reineke/indent-blankline.nvim'
Plug 'nvim-tree/nvim-web-devicons'

Plug 'catgoose/nvim-colorizer.lua'

Plug('neoclide/coc.nvim', { ['branch'] = 'release' })

Plug 'MeanderingProgrammer/render-markdown.nvim'

Plug('lewis6991/gitsigns.nvim')

vim.call('plug#end')

require('plugins.indent-blankline')
require('plugins.colorizer')
require('plugins.render-markdown')
