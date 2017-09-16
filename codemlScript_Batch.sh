#!/bin/bash

#########################################################################################################################
#This script was written by Nathan Whelan.

# THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE CONTRIBUTORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
# OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS WITH THE
# SOFTWARE.
##########################################################################################################################


##This shell script calls a simple for loop to automate codeml in combination with the script codemlScript.py This script was put together
##because there wasn't a very good way to call PAML in batch mode. This script could be useful if you have many gene alignments, 
##a tree for your taxa and the desire to fit your alignments and tree to a model in PAML. It could be used to test for positive
##selection for any given gene. NOTE: The tree must have the same tip names as taxa in the alignment. 

for FILE in *.phy.aln
do
NAME=`echo $FILE | sed 's/\_DNA.phy.aln//'`

##This needs to be modified given your naming schemes. 
python codemlScript.py $NAME\_DNA.phy.aln $NAME\_dropped.tre $NAME\_PAML_NeutralMethod1.out
done
