import React from "react";

// reactstrap components
import { Container } from "reactstrap";

// core components

function IndexHeader() {
  return (
    <>
      <div
        className="page-header section-dark"
        style={{
          backgroundImage:
            "url(" + require("assets/img/pexels-rodrigo-santos.jpg") + ")"
        }}
      >
        <div className="filter" />
        <div className="content-center">

          <Container>
            <div className="title-brand">
              <h1 className="presentation-title">Sentimenti</h1>
            </div>
            <h2 className="presentation-subtitle text-center">
              A search engine for KYC sentiment analysis
            </h2>
          </Container>
        </div>
        <div
          className="moving-clouds"
          style={{
            backgroundImage: "url(" + require("assets/img/clouds.png") + ")"
          }}
        />
        <h6 className="category category-absolute">
          Created by
          <a
            href="https://www.linkedin.com/in/pelle-ferment-871532146/"
            target="_blank"
          ><h6>Jarvin, Wei, Zhaohui and Pelle</h6>
          </a>
        </h6>
      </div>
    </>
  );
}

export default IndexHeader;
