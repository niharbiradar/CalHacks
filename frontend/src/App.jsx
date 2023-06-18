import styles from './style';

import { Navbar, Hero, Stats, Business, Billing, CardDeal, Footer} from './components';
import {Route, Routes} from "react-router-dom";

const App = () => (
  <div className="bg-primary w-full overflow-hidden">
    <div className={`${styles.paddingX} ${styles.flexCenter}`}>
      <div className={`${styles.boxWidth}`}>
        <Navbar></Navbar>
      </div>
    </div>

    <div className={`bg-primary ${styles.flexStart}`}>
      <div className={`${styles.boxWidth}`}>
        <Hero></Hero>
      </div>
    </div>

    <div className={`bg-primary ${styles.paddingX} ${styles.flexStart}`}>
      <div className={`${styles.boxWidth}`}>
        <Stats></Stats>
        <Business></Business>
        <Billing></Billing>
        <CardDeal></CardDeal> 
        <Footer></Footer>
      </div>
    </div>


  </div>
);

export default App