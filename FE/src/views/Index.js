import React from "react";

// reactstrap components

// core components
import IndexNavbar from "components/Navbars/IndexNavbar.js";
import IndexHeader from "components/Headers/IndexHeader.js";
import SearchField from "components/Body/SearchField.js";
import DemoFooter from "components/Footers/DemoFooter.js";

// index sections
import {isMobile} from 'react-device-detect';

function Index() {
  document.documentElement.classList.remove("nav-open");
  React.useEffect(() => {
    document.body.classList.add("index");
    return function cleanup() {
      document.body.classList.remove("index");
    };
  });

  if (isMobile) {
    return (
        <>
          <IndexNavbar />
          <IndexHeader />
          <SearchField />
          <div className="main">
            <DemoFooter />
          </div>
        </>
    );
  }

  return (
    <>
      <IndexNavbar />
      <IndexHeader />
      <SearchField />
      <div className="main">
        <DemoFooter />
      </div>
    </>
  );
}

export default Index;
