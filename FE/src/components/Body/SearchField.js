import React from "react";
import Search from "components/Body/Search.js";

// reactstrap components
import { Container } from "reactstrap";

// core components

function SearchField() {
  return (
    <>
      <div
        className="page-header section-dark"
      >

        <div className="filter" />
        <div className="content-center">
            <div className = "title-brand">
                <img src= "https://logos-world.net/wp-content/uploads/2021/08/Deloitte-Logo.png" width="40%" height="40%">
                </img>
             </div>
          <Container>
            <h2 className="presentation-subtitle text-center">
              Search a company for sentiment analysis
            </h2>
            <Container>
                <div className="text-center">
                    <br></br>
                    <Search></Search>
                </div>
            </Container>
          </Container>
        </div>
      </div>
    </>
  );
}

export default SearchField;
