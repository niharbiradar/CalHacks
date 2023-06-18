import { features } from '../constants';
import styles, { layout } from '../style';
import Button from './Button';

const Business = () => {
  return (
    <section id="features" className={layout.section}>
      <div className={layout.sectionInfo}>
        <h2 className={styles.heading2}>In The Battle of Ai Vs. DeepFakes, <br className="sm:block hidden" /> We Are The Winning Team</h2>
        <p></p>
      </div>
    </section>
  )

}

export default Business