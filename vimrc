let mapleader = " "

set cursorline
set norelativenumber
set number
set wrap
set showcmd
set wildmenu
set hlsearch
exec "nohlsearch"

set ignorecase
set incsearch
set smartcase

noremap = nzz
noremap - Nzz
noremap <LEADER><CR> :nohl<CR> 


 

syntax on

map S :w<CR>
map Q :q<CR>

map s <nop>
map R :source $MYVIMRC<CR>
