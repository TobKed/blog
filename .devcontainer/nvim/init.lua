vim.g.mapleader = " "
vim.o.wrap = true
vim.o.linebreak = true
vim.o.autoread = true
vim.api.nvim_create_autocmd({ "FocusGained", "BufEnter" }, { command = "checktime" })

vim.pack.add({
  { src = "https://github.com/MeanderingProgrammer/render-markdown.nvim", version = "v8.14.0" },
  { src = "https://github.com/stevearc/oil.nvim", version = "v2.16.0" },
  { src = "https://github.com/nvim-mini/mini.pick", version = "v0.18.0" },
}, { confirm = false })

-- no Nerd Font in the Codespaces browser terminal
require("render-markdown").setup({
  heading = { icons = {} },
  code = { language_icon = false },
  checkbox = { unchecked = { icon = "☐ " }, checked = { icon = "☑ " } },
  link = { enabled = false },
  sign = { enabled = false },
})
require("oil").setup({ columns = {} })
require("mini.pick").setup()

vim.keymap.set("n", "-", "<cmd>Oil<cr>")
vim.keymap.set("n", "<leader>f", "<cmd>Pick files<cr>")
vim.keymap.set("n", "<leader>/", "<cmd>Pick grep_live<cr>")
