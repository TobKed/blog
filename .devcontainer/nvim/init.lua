vim.g.mapleader = " "
vim.o.linebreak = true
-- reload files that an agent changes; checktime is not valid in the command-line window
vim.api.nvim_create_autocmd({ "FocusGained", "BufEnter", "CursorHold" }, {
  callback = function()
    if vim.fn.getcmdwintype() == "" then
      vim.cmd.checktime()
    end
  end,
})

-- commits, not tags: a tag can move (render-markdown v8.14.0, oil v2.16.0, mini.pick v0.18.0)
vim.pack.add({
  { src = "https://github.com/MeanderingProgrammer/render-markdown.nvim", version = "640a3ec6d538bad17c328be373c7cad0293d9589" },
  { src = "https://github.com/stevearc/oil.nvim", version = "17c0a8faaf48298a0c0cfb0d757c0eaee4ff7a32" },
  { src = "https://github.com/nvim-mini/mini.pick", version = "8c1f75f8ddd8c9f75d07ed2ab5718d2c3cb65a66" },
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
