# work_with_shafa_website
The project is designed for practice testing.
All project break into blocks: 
    test_all_inside, test_buttons_work,
    test_checking_colors, etc.

For this I took the https://shafa.ua/ web site.

For install all packages should install requirements file.
For this should use command pip install -r requirements.txt

  1) Run test
     pytest -svx + path to file

  2) Active environment
     source env/bin/activate

  3) Check tests
     flake8 test_len_elements/+file name
   
  4) Run regression 
     pytest -svx /home/iryna/Documents/work_with_shafa_website/
                 (path to scope files)
     example:
     pytest -svx D:\work_with_shafa_website\tests\test_006.py
