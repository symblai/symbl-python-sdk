# coding: utf-8

"""
    symbl.ai APIs

    <h1>Symbl's APIs for external consumers.</h1> <h2>Language Insights API</h2> Symbl's Language Insights API provides an interface for applications to perform the analysis on the raw text and get insights from it. The API automatically detects sentence boundaries and punctuates the sentences, and also returns the updated messages in the response. Conversations are the most unstructured piece of information that we represent information in, and which most of the leads to lot of loss of information by not being able to capture them correctly.<br/> Language Insights API focuses on understanding such texts and generate the useful and important information from them. <br/> Currently the API supports detection of the Action Items in any type of unstructured text. In future the same API will also have support to detect \"Information\" and \"Event\", where Information is any informational piece and Event is a reference to something that has happened in the past.<br/> <h2>Telephony Integration</h2> Symbl can currently integrate with two types of telephony endpoints: 1. SIP trunks<br/> 2. PSTN endpoints<br/> Results are sent via HTTP WebHooks as and when they are available.<br/> <h2>Flow</h2> 1. External Application invokes REST API to join a meeting/session, with the mode (SIP/PSTN) and joining details<br/> 2. Symbl joins the meeting via SIP or PSTN integration<br/> 3. Symbl continuously processes the audio stream received<br/> 4. Symbl calls WebHook whenever transcription results are available<br/>  # noqa: E501

    Contact: info@symbl.ai
"""

from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools


setup(
    name="symbl",
    version="1.0.12",
    description="symbl.ai SDK",
    author_email="info@symbl.ai",
    url="",
    keywords=["Symbl.ai SDK"],
    install_requires=["symbl_rest >= 1.0.6", "websocket-client >= 0.59.0", "sounddevice >= 0.4.1", "numpy"],
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    &lt;h1&gt;Symbl&#x27;s APIs for external consumers.&lt;/h1&gt; &lt;h2&gt;Language Insights API&lt;/h2&gt; Symbl&#x27;s Language Insights API provides an interface for applications to perform the analysis on the raw text and get insights from it. The API automatically detects sentence boundaries and punctuates the sentences, and also returns the updated messages in the response. Conversations are the most unstructured piece of information that we represent information in, and which most of the leads to lot of loss of information by not being able to capture them correctly.&lt;br/&gt; Language Insights API focuses on understanding such texts and generate the useful and important information from them. &lt;br/&gt; Currently the API supports detection of the Action Items in any type of unstructured text. In future the same API will also have support to detect \&quot;Information\&quot; and \&quot;Event\&quot;, where Information is any informational piece and Event is a reference to something that has happened in the past.&lt;br/&gt; &lt;h2&gt;Telephony Integration&lt;/h2&gt; Symbl can currently integrate with two types of telephony endpoints: 1. SIP trunks&lt;br/&gt; 2. PSTN endpoints&lt;br/&gt; Results are sent via HTTP WebHooks as and when they are available.&lt;br/&gt; &lt;h2&gt;Flow&lt;/h2&gt; 1. External Application invokes REST API to join a meeting/session, with the mode (SIP/PSTN) and joining details&lt;br/&gt; 2. Symbl joins the meeting via SIP or PSTN integration&lt;br/&gt; 3. Symbl continuously processes the audio stream received&lt;br/&gt; 4. Symbl calls WebHook whenever transcription results are available&lt;br/&gt;  # noqa: E501
    """
)
