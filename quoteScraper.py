import pyautogui as pag
import pyperclip as clip
import time

time.sleep(0.5)


file_path = '/Users/ddormac/vscode/html/quoteGeneratorSite/quoteInfo.txt'
file = open(file_path, 'a')

#starting location
xLoc = 683
yLoc = 740
# goes to the correct screen
pag.click(xLoc,yLoc)


for i in range(10):
    # clicks share
    xLoc = 683
    yLoc = 740
    pag.click(xLoc,yLoc)

    time.sleep(1)

    # goes to message button and clicks
    xLoc = 520
    yLoc = 680
    pag.click(xLoc,yLoc)

    time.sleep(1)

    # goe to copy button and clicks
    xLoc = 640
    yLoc = 540
    pag.click(xLoc,yLoc)

    time.sleep(2)

    # More reliable way of copying the quote and the author
    content = clip.paste()
    quote, *rest = content.split('\n', 1)

    # Remove leading and trailing whitespaces from the quote
    quote = quote.strip()

    # Assign None to the author if it is not present
    author = None

    # Check if there is a second element in the `rest` list
    if len(rest) > 0:
        author_with_link = rest[0].strip()
        
        # Remove the link from the author
        author = author_with_link.split(':')[0]

    # sets content equal to what is currently copied and a new line
    content = quote + " " + author + '\n'
    content = content.split("From the Motivation app")[0].strip()

    # writes copied text into txt file
    file.write(content + '\n')

    time.sleep(2)

    pag.press('up')

    time.sleep(2)

file.close()