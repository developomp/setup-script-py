" auto-install vim-plug
if empty(glob('~/.vim/autoload/plug.vim'))
	silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
		https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
endif

call plug#begin('~/.vim/plugged')

	Plug 'jiangmiao/auto-pairs'						"auto pairs for '(' '[' '{'
	Plug 'joshdick/onedark.vim'						"theme
	Plug 'preservim/nerdtree'						"File explorer
	Plug 'Xuyuanp/nerdtree-git-plugin'				"nerdtree git status
	Plug 'Xuyuanp/nerdtree-git-plugin'				"show git status in nerdtree
	Plug 'tiagofumo/vim-nerdtree-syntax-highlight'	"file/folder icons in nerdtree
	Plug 'ryanoasis/vim-devicons'					"icons
	Plug 'vim-airline/vim-airline'					"bottom bar
	Plug 'sheerun/vim-polyglot'						"common langauge syntax
	Plug 'prettier/sbdchd/neoformat'				"code formatting

	Plug 'KabbAmine/vCoolor.vim'					"color picker
	Plug 'lilydjwg/colorizer'						"highlight color values (rgb, hex, etc.)

	Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }	"Golang support

call plug#end()

" auto format on save
augroup fmt
  autocmd!
  autocmd BufWritePre * undojoin | Neoformat
augroup END

" Configuration

syntax on							"enable language-based coloring
colorscheme onedark					"set color scheme
let g:airline_theme='onedark'		"set airline theme

set number							"show line number
set encoding=UTF-8					"set encoding to UTF-8
set noerrorbells					"no sound effects
set tabstop=4 softtabstop=4			"how many spaces a tab should use
set shiftwidth=4					"number of spaces to indent/outdent with >>/<<
set wildmenu						"command completion
set autoindent						"automatically add indent
set smartindent						"language aware indention
set noexpandtab						"do not convert tab to spaces
set nowrap							"disable text wrap
set smartcase						"ignore case when searching except when there is a capital letter in the query
set noswapfile						"no swap file (vim creates them by default) 
set nobackup						"do not create a temporary backup file
set hlsearch						"highlight all matching pattern when searching
noh									"clear highlight when search pattern is empty
set formatoptions-=c				"don't extend comment to new line
set formatoptions-=r				"same as line above
set formatoptions-=o				"same as line above

" Keybinds

map			<c-s>		:w<CR>|					"save on ctrl+s
map			<a-Up>		:m-2<CR>gv=gv|			"move selected lines up one line
map			<a-Down>	:m'>+<CR>gv=gv|			"move selected lines down one line
nnoremap	<C-t>		:NERDTreeToggle<CR>|	"toggle nerdtree visibility
nnoremap	<C-f>		:NERDTreeFind<CR>|		"find in nerdtree
