Quizdown Demo
=============

Embed an external quizfile
+++++++++++++++++++++++++++

.. code:: rst

   .. quizdown:: ./quiz.md


.. raw:: html

   <details>
   <summary><a>🤖 Show <code>quiz.md</code></a></summary>

.. literalinclude :: quiz.md
   :language: md

.. raw:: html

   </details>


Rendered quiz app (🚀 edit_ in quizdown editor)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _edit: https://bonartm.github.io/quizdown-live-editor/?code=---%0Ashuffle_answers%3A%20true%0Ashuffle_questions%3A%20false%0Alocale%3A%20en%0A---%0A%0A%23%23%23%23%20Who%20is%20the%20person%20in%20the%20picture%3F%0A%0A!%5B%5D(https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F9%2F9d%2FSir_Tim_Berners-Lee.jpg%2F330px-Sir_Tim_Berners-Lee.jpg)%0A%0A%3E%20In%201990%2C%20he%20published%20the%20%5Bworlds%20first%20website%5D(http%3A%2F%2Finfo.cern.ch%2Fhypertext%2FWWW%2FTheProject.html).%0A%0A-%20%5Bx%5D%20Tim%20Berners-Lee%0A-%20%5B%20%5D%20Alan%20Turing%0A-%20%5B%20%5D%20Barbara%20Liskov%0A-%20%5B%20%5D%20Larry%20Page%0A%0A%0A%23%23%23%23%20Who%20is%20the%20person%20in%20the%20picture%3F%0A%0A!%5B%5D(https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Fe%2Fe5%2FTed_Nelson_cropped.jpg%2F330px-Ted_Nelson_cropped.jpg)%0A%0A%3E%20He%20coined%20the%20terms%20*hyptertext*%20and%20*hypermedia*%20in%201963!%0A%0A-%20%5Bx%5D%20Ted%20Nelson%0A-%20%5B%20%5D%20Donald%20Knuth%0A-%20%5B%20%5D%20Grace%20Hopper%0A-%20%5B%20%5D%20John%20von%20Neumann%0A%0A%0A%23%23%23%23%20What%20is%20the%20HTML%20element%20for%20the%20largest%20heading%20in%20a%20document%3F%0A%0A-%20%5Bx%5D%20%60%3Ch1%3E%3C%2Fh1%3E%60%0A-%20%5B%20%5D%20%60%3Cheader%3E%3C%2Fheader%3E%60%0A-%20%5B%20%5D%20%60%3Ctitle%3E%3C%2Ftitle%3E%60%0A-%20%5B%20%5D%20%60%3Cheading1%3E%3C%2Fheading1%3E%60%0A%0A%0A%0A%23%23%23%23%20What%20is%20the%20%60%3Ca%3E%3C%2Fa%3E%60%20tag%20used%20for%3F%0A%0A-%20%5Bx%5D%20for%20defining%20hyperlinks%0A-%20%5B%20%5D%20for%20defining%20a%20paragraph%0A-%20%5B%20%5D%20for%20defining%20code%20snippet%0A-%20%5B%20%5D%20for%20defining%20an%20image%0A%0A%0A%0A%23%23%23%20What%20is%20the%20difference%20between%20a%20tag%20and%20an%20attribute%3F%0A%0A%60%60%60html%0A%3Ca%20href%3D%22url%22%3Elink%20text%3C%2Fa%3E%0A%60%60%60%0A%0ASelect%20all%20correct%20answers%3A%0A%0A-%20%5Bx%5D%20A%20tag%20represents%20an%20html%20element.%0A-%20%5Bx%5D%20An%20attribute%20defines%20a%20property%20of%20an%20html%20element.%0A-%20%5B%20%5D%20An%20attribute%20is%20everything%20between%20the%20opening%20and%20closing%20tag.%0A-%20%5B%20%5D%20%60%22url%22%60%20is%20an%20attribute%20in%20the%20example%20above.%0A%0A%0A%23%23%23%23%20How%20many%20valid%20HTML%20element%20tags%20are%20currently%20defined%3F%0A%0A%3E%20Check%20out%20https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FElement%0A%0A-%20%5Bx%5D%20100%20-%20120%0A-%20%5B%20%5D%2080%20-%20100%0A-%20%5B%20%5D%20120%20-%20140%0A-%20%5B%20%5D%20140%20-%20160%0A%0A%0A%23%23%23%20How%20many%20%60buttons%60%20are%20defined%20on%20the%20%5Bhomepage%20of%20Spiced%20Academy%5D(https%3A%2F%2Fwww.spiced-academy.com%2Fen)%3F%0A%0A%60%60%60html%0A%3Cbutton%3E%0A%20%20%20%20my%20button%0A%3C%2Fbutton%3E%0A%60%60%60%0A%0A-%20%5Bx%5D%207%0A-%20%5B%20%5D%2014%0A-%20%5B%20%5D%205%0A-%20%5B%20%5D%2023%0A%0A%0A%23%23%23%23%20What%20is%20the%20IP%20address%20of%20%5Bgoogle.com%5D(https%3A%2F%2Fgoogle.com)%3F%0A%0A-%20%5Bx%5D%20142.250.186.110%0A%20%20%20%20%3E%20This%20is%20the%20ipv4%20address%0A-%20%5Bx%5D%202a00%3A1450%3A4001%3A829%3A%3A200e%0A%20%20%20%20%3E%20This%20is%20the%20ipv6%20address%0A-%20%5B%20%5D%20https%0A-%20%5B%20%5D%20com%0A%0A%0A%23%23%23%23%20What%20is%20a%20tag%20soup%3F%0A%0A%3E%20%60%3Cp%3EThis%20is%20a%20tag%20%3Cem%3Esoup.%3C%2Fp%3E%3C%2Fem%3E%60%0A%0A-%20%5B%20%5D%20nicely%20written%20html%20code%0A-%20%5Bx%5D%20malformed%20html%20code%0A%0A%0A%0A%23%23%23%23%20Two%20organizations%20hide%20in%20the%20chunk%20of%20text.%20Do%20you%20find%20them%3F%0A%0A%60%60%60%0ACW3THAGWW%0A%60%60%60%0A%0A-%20%5Bx%5D%20%60W3C%60%0A%20%20%20%20%3E%20World%20Wide%20Web%20Consortium%0A-%20%5Bx%5D%20%60WHATWG%60%0A%20%20%20%20%3E%20Web%20Hypertext%20Application%20Technology%20Working%20Group%0A-%20%5B%20%5D%20%60WWW%60%0A-%20%5B%20%5D%20%60C3PO%60

.. quizdown:: ./quiz.md

----

Write inline quizdown
+++++++++++++++++++++


.. code:: rst

   .. quizdown::

      ---
      shuffle_answers: false
      ---

      ## What is the capital of Germany?

      > It's the largest city in Germany.  

      1. [x] Berlin
      2. [ ] Cologne
      3. [ ] Frankfurt
      4. [ ] Munich


Rendered quiz app
~~~~~~~~~~~~~~~~~

.. quizdown::

   ---
   shuffle_answers: false
   ---

   ## What is the capital of Germany?

   > It's the largest city in Germany.  

   1. [x] Berlin
   2. [ ] Cologne
   3. [ ] Frankfurt
   4. [ ] Munich





