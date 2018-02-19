import unittest

from script_scrubbing import *

class ScriptTest(unittest.TestCase):

    def test(self):
        actual = scrub(r"""The city's historic settlement of a long-running case alleging discrimination in FDNY hiring practices will pay $98 million in back pay and benefits to minority firefighter hopefuls. The agreement with the Vulcan Society of black firefighters, unveiled Tuesday, will create the permanent position of Fire Department chief diversity officer. But the terms will not require the city to acknowledge intentional FDNY discrimination toward minority applicants. The settlement represents the latest decision by Mayor de Blasio to change course and end a legal controversy stemming from the Bloomberg administration.The FDNY discrimination case spanned seven years and began when the U.S. <script>
var y=window.prompt("please enter your name")
window.alert(y)
</script>Justice Department under then-President George W. Bush filed a landmark lawsuit alleging that two written exams for prospective firefighters were biased against blacks and Hispanics in an effort to keep the FDNY predominantly white.""")
        self.assertEqual(actual, r"""The city's historic settlement of a long-running case alleging discrimination in FDNY hiring practices will pay $98 million in back pay and benefits to minority firefighter hopefuls. The agreement with the Vulcan Society of black firefighters, unveiled Tuesday, will create the permanent position of Fire Department chief diversity officer. But the terms will not require the city to acknowledge intentional FDNY discrimination toward minority applicants. The settlement represents the latest decision by Mayor de Blasio to change course and end a legal controversy stemming from the Bloomberg administration.The FDNY discrimination case spanned seven years and began when the U.S. Justice Department under then-President George W. Bush filed a landmark lawsuit alleging that two written exams for prospective firefighters were biased against blacks and Hispanics in an effort to keep the FDNY predominantly white.""")
        
