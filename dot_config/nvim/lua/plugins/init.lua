local Plug = vim.fn['plug#']

vim.call('plug#begin')

Plug('nvim-treesitter/nvim-treesitter', {['do'] = ':TSUpdate'})
Plug 'nvim-treesitter/nvim-treesitter-context'
Plug 'lukas-reineke/indent-blankline.nvim'
Plug 'nvim-tree/nvim-web-devicons'
Plug('akinsho/bufferline.nvim', {['tag'] = '*'})

Plug 'catgoose/nvim-colorizer.lua'

Plug 'nvim-tree/nvim-tree.lua'
Plug 'nvim-tree/nvim-web-devicons'

Plug('neoclide/coc.nvim', { ['branch'] = 'release' })

Plug 'nvim-mini/mini.nvim'
Plug 'MeanderingProgrammer/render-markdown.nvim'

Plug 'lilydjwg/fcitx.vim'

vim.call('plug#end')

require('plugins.indent-blankline')
require('plugins.colorizer')
require('plugins.bufferline')
require('plugins.nvim-tree')
require('plugins.render-markdown')
