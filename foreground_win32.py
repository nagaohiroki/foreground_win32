import win32gui
def activate_win32(hwnd, _):
    win_name = win32gui.GetWindowText(hwnd)
    if win_name.endswith('NVIM') or win_name == 'Neovim':
       win32gui.SetForegroundWindow(hwnd)

if __name__ == '__main__':
    win32gui.EnumWindows(activate_win32, None)
