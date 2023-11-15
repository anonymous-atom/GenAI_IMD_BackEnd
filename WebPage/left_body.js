import React from "react";
import { Card, CardContent, Button, Container } from "@material-ui/core";

const App = () => {
  // Sample card data
  const cards = [
    {
      title: "Summary",
      content: "This is a brief summary of the content.",
    },
    {
      title: "Examples",
      content: "Here are a few examples of the content.",
    },
    {
      title: "In-depth Text",
      content:
        "This section provides detailed in-depth information about the content.",
    },
    {
      title: "Practice Questions",
      content: "Practice questions to test your knowledge.",
    },
  ];

  // Function to copy text from a card
  const copyText = (text) => {
    // Implement your copy text logic here
  };

  return (
    <Container maxWidth="md">
      <div className="scrollable-container">
        <div className="scrollable-cards">
          {cards.map((card, index) => (
            <Card key={index} className="card">
              <CardContent>
                <h3>{card.title}</h3>
                <div className="horizontal-scroll-content">
                  <p>{card.content}</p>
                </div>
                <Button
                  variant="contained"
                  color="primary"
                  onClick={() => copyText(card.content)}
                >
                  Copy Text
                </Button>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </Container>
  );
};

export default App;
