import os
import time

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def show_banner():
    print(f"{Colors.CYAN}")
    print("  ════════════════════════════════════════════════════════════")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}           ██████╗ ██████╗ ██╗████████╗ ██████╗           {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}          ██╔═══██╗██╔══██╗██║╚══██╔══╝██╔═══██╗          {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}          ██║   ██║██████╔╝██║   ██║   ██║   ██║          {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}          ██║   ██║██╔══██╗██║   ██║   ██║   ██║          {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}          ╚██████╔╝██████╔╝██║   ██║   ╚██████╔╝          {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}           ╚═════╝ ╚═════╝ ╚═╝   ╚═╝    ╚═════╝           {Colors.CYAN}")
    print("  ────────────────────────────────────────────────────────")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}                O B I T Ō   C I P H E R                  {Colors.CYAN}")
    print("  ────────────────────────────────────────────────────────")
    print(f"  {Colors.YELLOW}            Caesar Cipher Tool v1.0                  {Colors.CYAN}")
    print(f"  {Colors.GREEN}              Secure Text Transformation              {Colors.CYAN}")
    print("  ════════════════════════════════════════════════════════════")
    print(f"{Colors.END}")

    print(f"{Colors.BLUE}{'═' * 60}{Colors.END}")
    print(f"{Colors.WHITE}    Secure  •  Fast  •  Interactive  •  Reliable{Colors.END}")
    print(f"{Colors.BLUE}{'═' * 60}{Colors.END}\n")

chars = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_character_map_with_animation(start_pos, end_pos, shift, operation_type, current_char, result_char):
    print(f"{Colors.CYAN}Caesar Cipher Animation - {operation_type.title()}{Colors.END}")
    print(f"{Colors.BLUE}══════════════════════════════════════════════{Colors.END}")
    
    # Show positions
    print("    ", end="")
    for i in range(13):
        if i < 10:
            print(f" {i}  ", end="")
        else:
            print(f" {i} ", end="")
    
    print("\n    ", end="")
    
    # First row animation
    for i, char in enumerate(chars[:13]):
        if i == start_pos:
            if operation_type == "encode":
                print(f"{Colors.GREEN}▶{char}◀{Colors.END}", end="")
            else:
                print(f"{Colors.YELLOW}▶{char}◀{Colors.END}", end="")
        elif i == end_pos:
            print(f"{Colors.MAGENTA}[{char}]{Colors.END}", end=" ")
        else:
            print(f" {char}  ", end="")
    
    print("\n    ", end="")
    for i in range(13, 26):
        print(f" {i} ", end="")
    
    print("\n    ", end="")
    
    # Second row animation
    for i, char in enumerate(chars[13:], 13):
        if i == start_pos:
            if operation_type == "encode":
                print(f"{Colors.GREEN}▶{char}◀{Colors.END}", end="")
            else:
                print(f"{Colors.YELLOW}▶{char}◀{Colors.END}", end="")
        elif i == end_pos:
            print(f"{Colors.MAGENTA}[{char}]{Colors.END}", end=" ")
        else:
            print(f" {char} ", end=" ")
    
    print(f"\n{Colors.BLUE}══════════════════════════════════════════════{Colors.END}")
    
    # Show movement direction
    if operation_type == "encode":
        direction = "→"
        color = Colors.GREEN
        movement_text = f"Moving forward by {shift} positions"
    else:
        direction = "←"
        color = Colors.YELLOW
        movement_text = f"Moving backward by {shift} positions"
    
    print(f"{color}{movement_text}{Colors.END}")
    print(f"{Colors.WHITE}Path: {current_char}[{start_pos}] {direction} {result_char}[{end_pos}]{Colors.END}")

def animate_movement(start_pos, end_pos, shift, operation_type, current_char, result_char):
    """Animate the movement from start to end position"""
    current = start_pos
    
    if operation_type == "encode":
        step = 1
        color = Colors.GREEN
    else:
        step = -1
        color = Colors.YELLOW
    
    # Calculate the path
    if operation_type == "encode":
        if start_pos <= end_pos:
            path = list(range(start_pos, end_pos + 1))
        else:
            path = list(range(start_pos, 26)) + list(range(0, end_pos + 1))
    else:
        if start_pos >= end_pos:
            path = list(range(start_pos, end_pos - 1, -1))
        else:
            path = list(range(start_pos, -1, -1)) + list(range(25, end_pos - 1, -1))
    
    # Show animation steps - SLOWER VERSION
    for i, pos in enumerate(path):
        clear_screen()
        show_banner()
        
        if i == len(path) - 1:
            # Final position
            show_character_map_with_animation(pos, end_pos, shift, operation_type, current_char, result_char)
            print(f"\n{color}✓ Transformation Complete: {current_char} → {result_char}{Colors.END}")
        else:
            # Moving position
            show_character_map_with_animation(pos, end_pos, shift, operation_type, current_char, result_char)
            print(f"\n{color}↝ Moving... ({i+1}/{len(path)}){Colors.END}")
        
        # إبطاء الحركة - زيادة وقت الانتظار
        time.sleep(0.8)  # Changed from 0.3 to 0.8 seconds

def process_text(text, shift, operation):
    text = text.upper().replace(" ", "")
    result_text = ""

    print(f"\n{Colors.MAGENTA}Input: {Colors.WHITE}{text}{Colors.END}")
    print(f"{Colors.YELLOW}Shift: {shift}{Colors.END}")
    print(f"{Colors.BLUE}────────────────────────────────────────────{Colors.END}")

    for i, char in enumerate(text):
        if char in chars:
            text_pos = chars.index(char)

            if operation == "encode":
                result_pos = (text_pos + shift) % len(chars)
                operation_name = "Encoding"
                color = Colors.GREEN
            else:
                result_pos = (text_pos - shift) % len(chars)
                operation_name = "Decoding"
                color = Colors.YELLOW

            result_char = chars[result_pos]

            print(f"\n{color}{operation_name}: '{char}' -> '{result_char}'{Colors.END}")
            print(f"{Colors.WHITE}Position: {text_pos} -> {result_pos}{Colors.END}")

            # Show animated movement - SLOWER
            animate_movement(text_pos, result_pos, shift, operation, char, result_char)
            
            # زيادة وقت الانتظار بين الحروف
            time.sleep(1.5)  # Changed from 1 to 1.5 seconds
            result_text += result_char

    return result_text

def show_character_map(highlight_positions=[], target_positions=[], title="Caesar Cipher Table", operation_type="encode"):
    """Static character map display"""
    print(f"{Colors.CYAN}{title}{Colors.END}")
    print(f"{Colors.BLUE}══════════════════════════════════════════════{Colors.END}")

    print("    ", end="")
    for i in range(13):
        if i < 10:
            print(f" {i}  ", end="")
        else:
            print(f" {i} ", end="")

    print("\n    ", end="")
    for i, char in enumerate(chars[:13]):
        if i in highlight_positions:
            if operation_type == "encode":
                print(f"{Colors.GREEN}▶{char}◀{Colors.END}", end="")
            else:
                print(f"{Colors.YELLOW}▶{char}◀{Colors.END}", end="")
        elif i in target_positions:
            print(f"{Colors.MAGENTA}[{char}]{Colors.END}", end=" ")
        else:
            print(f" {char}  ", end="")

    print("\n    ", end="")
    for i in range(13, 26):
        print(f" {i} ", end="")

    print("\n    ", end="")
    for i, char in enumerate(chars[13:], 13):
        if i in highlight_positions:
            if operation_type == "encode":
                print(f"{Colors.GREEN}▶{char}◀{Colors.END}", end="")
            else:
                print(f"{Colors.YELLOW}▶{char}◀{Colors.END}", end="")
        elif i in target_positions:
            print(f"{Colors.MAGENTA}[{char}]{Colors.END}", end=" ")
        else:
            print(f" {char} ", end=" ")

    print(f"\n{Colors.BLUE}══════════════════════════════════════════════{Colors.END}")

def main():
    while True:
        clear_screen()
        show_banner()

        show_character_map([], [], "Caesar Cipher Table - Ready")

        print(f"\n{Colors.GREEN}1. Encode text{Colors.END}")
        print(f"{Colors.GREEN}2. Decode text{Colors.END}")
        print(f"{Colors.MAGENTA}3. Demo: 'HELLO' with shift 3{Colors.END}")
        print(f"{Colors.RED}4. Exit{Colors.END}")

        choice = input(f"\n{Colors.WHITE}Choose option (1-4): {Colors.END}")

        if choice == "1":
            text = input(f"\n{Colors.WHITE}Enter text to encode: {Colors.END}")
            try:
                shift = int(input(f"{Colors.WHITE}Enter shift value: {Colors.END}"))
                result = process_text(text, shift, "encode")
                print(f"\n{Colors.GREEN}{Colors.BOLD}FINAL RESULT:{Colors.END}")
                print(f"{Colors.CYAN}Input:  {text}{Colors.END}")
                print(f"{Colors.YELLOW}Shift:  {shift}{Colors.END}")
                print(f"{Colors.GREEN}Output: {result}{Colors.END}")
                input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.END}")
            except ValueError:
                print(f"{Colors.RED}Invalid shift value!{Colors.END}")
                time.sleep(2)

        elif choice == "2":
            text = input(f"\n{Colors.WHITE}Enter text to decode: {Colors.END}")
            try:
                shift = int(input(f"{Colors.WHITE}Enter shift value: {Colors.END}"))
                result = process_text(text, shift, "decode")
                print(f"\n{Colors.GREEN}{Colors.BOLD}FINAL RESULT:{Colors.END}")
                print(f"{Colors.CYAN}Input:  {text}{Colors.END}")
                print(f"{Colors.YELLOW}Shift:  {shift}{Colors.END}")
                print(f"{Colors.GREEN}Output: {result}{Colors.END}")
                input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.END}")
            except ValueError:
                print(f"{Colors.RED}Invalid shift value!{Colors.END}")
                time.sleep(2)

        elif choice == "3":
            print(f"\n{Colors.MAGENTA}Running demo: 'HELLO' with shift 3{Colors.END}")
            time.sleep(2)
            result = process_text("HELLO", 3, "encode")
            print(f"\n{Colors.GREEN}Demo Complete! 'HELLO' -> '{result}'{Colors.END}")
            input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.END}")

        elif choice == "4":
            print(f"{Colors.CYAN}Goodbye!{Colors.END}")
            break

        else:
            print(f"{Colors.RED}Invalid choice!{Colors.END}")
            time.sleep(1)

if __name__ == "__main__":
    main()