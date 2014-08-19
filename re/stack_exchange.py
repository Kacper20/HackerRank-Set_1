import re
import sys


stri = '''<div class="question-summary" id="question-summary-80407">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>2</strong></span>
                    <div class="viewcount">votes</div>
                </div>
            </div>
            <div class="status answered">
                <strong>1</strong>answer
            </div>
        </div>



<div class="views " title="60 views">
                    60 views
</div>
    </div>
    <div class="summary">        
        <h3>[about power supply of opertional amplifier](/questions/80407/about-power-supply-of-opertional-amplifier)</h3>
        <div class="excerpt">
            I am constructing an operational amplifier as shown in the following figure. I use a batter as supplier for the OP Amp and set it up as a non-inverting amp circuit. I saw that the output was clipped ...
        </div>

        <div class="tags t-op-amp">
            [op-amp](/questions/tagged/op-amp "show questions tagged 'op-amp'") 

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 21:49:14Z" class="relativetime">11 hours ago</span>
        </div>
        <div class="user-gravatar32">'''
       
identifier = re.findall(r'id="question-summary-(\d+)"[.\n]+<h3>\[(.+)\][.\n]+asked .+class="relativetime">(.+)</span', stri)
print identifier