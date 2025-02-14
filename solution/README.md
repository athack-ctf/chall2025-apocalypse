# How to Solve the Challenge?

(1) `[physicslab.webp]` picture is first given to participants. There is nothing hidden in the page. Then, you check the http link. You found `/page1` at the end of the http link, so you wonder what `/page2` is like. So you look for `/page2`.

(2) In `/page2`, you will see professor Weasley asking you to eat somthing to prove that you are a human and not a robot. There is a hint in the picture -> the prof is giving you a cookie. So, you manipulate the web cookie with key `is_human` by setting its value to `true`

(3) In `/human`, you will see the password in a comment if you inspect the page. `body > div > form > input[type="password"]:nth-child(2)`

(5) In `/emp`, the answer for the next sequence is 1081 and it is the code to set off EMP. Here is the link for how to solve the next sequence https://alteredqualia.com/visualization/hn/sequence/

(4) In `/files`, the flag is hidden in the setting of EMP file.

