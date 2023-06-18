import styles from './style';

import { Dashbar, DashHero, DfList} from './components';


const Dashboard = () => (
  <div className="bg-primary w-full overflow-hidden">
    <div className={`${styles.paddingX} ${styles.flexCenter}`}>
      <div className={`${styles.boxWidth} -mb-12 `}>
        <Dashbar></Dashbar>
      </div>
    </div>

    <div className={`bg-primary ${styles.flexStart}`}>
      <div className={`${styles.boxWidth}`}>
        <DashHero></DashHero>
      </div>
      <div>
      </div>
      
    </div>
    <div>
        <DfList></DfList>
    </div>

  </div>
    
  
);

export default Dashboard