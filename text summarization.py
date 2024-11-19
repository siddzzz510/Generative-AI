import openai

# Set your OpenAI API key here
openai.api_key = "sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA"
def summarize_meeting(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that summarizes meeting minutes."},
            {"role": "user", "content": f"Summarize the following meeting minutes in 4 bullet points:\n\n{text}"}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].message['content'].strip()

# Meeting minutes text
meeting_minutes = """
Car Manufacturing Company Board of Directors Meeting Minutes
Agenda:
1. Call to Order
2. Approval of Previous Meeting Minutes
3. CEO's Report
4. Financial Report
Meeting Minutes:
1. Call to Order:
- The meeting was called to order by Bharath Thippireddy.
2. Approval of Previous Meeting Minutes:
- The minutes of the previous board meeting, held on [Date], were reviewed and approved.
3. CEO's Report:
- Bharath Thippireddy presented an overview of the company's performance, highlighting key achievements and challenges. Key points discussed include:
- Sales figures for the last quarter.
- Progress on cost reduction initiatives.
- Highlights from recent industry events.
- The CEO answered questions from board members.
4. Financial Report:
- The Chief Financial Officer ([CFO's Name]) presented the financial report. Key financial metrics discussed include:
- Revenue and profit margins.
- Budget vs. actual expenditure.
- Cash flow analysis.
- The board discussed financial performance and the impact on shareholder value.
"""

# Get the summarized response
summary = summarize_meeting(meeting_minutes)
print("Meeting Summary:")
print(summary)
