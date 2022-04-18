import "./App.css";
import NavBar from "./components/NavBar";
import SiteHeader from "./components/SiteHeader";
import { Route, Routes } from "react-router-dom";
import Dictionary from "./components/Pages/Dictionary";
import AboutUs from "./components/Pages/AboutUs";
import ContactUs from "./components/Pages/ContactUs";
import Contributors from "./components/Pages/Contributors";
import SearchPage from "./components/Pages/SearchPage";
import Footer from "./components/Footer";

function App() {
  return (
    <div className="App">
      <SiteHeader />
      <NavBar />
      <Routes>
        <Route exact path="/" element={<Dictionary />} />
        <Route path="/about" element={<AboutUs />} />
        <Route path="/contact" element={<ContactUs />} />
        <Route path="/contributors" element={<Contributors />} />
        <Route path="/search" element={<SearchPage />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
