from playwright.sync_api import Page , expect

def test_frames(page: Page):

     page.goto("https://ui.vision/demo/webtest/frames/")

     # Count number of frames
     frames=page.frames
     print("Number of frames on a page:", len(frames))  # 7

     # frame 1
     # we can use below three options

     # option 1: get the frame using css
     # frame1 = page.frame_locator("frame[src='frame_1.html']")

     # option 2: get the frame using url
     # frame1 = page.frame(url='https://ui.vision/demo/webtest/frames/frame_1.html')

     # options 3: get the frame using name (We cannot use here as we do not have name attribute for the frame 1
     # frame1 = page.frame("name of the frame")

     # we will use option 2: get the frame using url
     # here we have used chaining of locator for second statement (frame1)
     frame1 = page.frame(url='https://ui.vision/demo/webtest/frames/frame_1.html')
     inputbox = frame1.locator("input[name='mytext1']")
     inputbox.fill("Welcome")

     expect(inputbox).to_have_value("Welcome")

     page.wait_for_timeout(5000)



def test_inner_frames(page: Page):
     page.goto("https://ui.vision/demo/webtest/frames/")

     # grab the frame 3 (2 options below) for child frames better to go with 2nd option
     # option - 1 = frame3=page.frame_locator("frame[src='frame_3.html']")
     # option - 2 = frame3=page.frame(url="https://ui.vision/demo/webtest/frames/frame_3.html")

     frame3 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3.html")

     # get the inputbox from frame 3 and provide the text
     frame3.locator("input[name='mytext3']").fill("Welcome")

     # Count number of frames
     child_frames=frame3.child_frames
     print("Number of child frames inside the frame 3: ", len(child_frames))

     # 0 is index
     innerframe=child_frames[0]

     # here we accessed child frame and used get_by_label
     radiobutton=innerframe.get_by_label("I am a human")
     radiobutton.check()
     expect(radiobutton).to_be_checked()

     page.wait_for_timeout(5000)