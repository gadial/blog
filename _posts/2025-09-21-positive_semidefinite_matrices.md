---
title: "מטריצות חיוביות"
layout: post
categories:
  - אלגברה לינארית
tags:
  - מטריצות חיוביות
---


<h2>מבוא</h2>

נושא בסיסי באלגברה לינארית שעדיין לא יצא לי לדבר עליו בפוסט הוא <strong>מטריצות חיוביות</strong> ומטריצות <strong>חיוביות לחלוטין</strong>. באנגלית מטריצות כאלו נקראות Positive Semidefinite ו-Positive Definite ובעברית מאוד מקובל השם "מטריצה מוגדרת אי-שלילית" ו"מטריצה מוגדרת חיובית" שאני לא אוהב אז אני אדבוק כאן בשמות הקצרים יותר. סיימנו מהר את הדיון הכואב על הטרמינולוגיה ואפשר לעבור לדבר על מה זה בכלל.

נקודת מוצא טובה לנושא היא המושג של <strong>מכפלה פנימית</strong>. כזכור, יש לנו מרחב וקטורי {% equation %}V{% endequation %} מעל שדה {% equation %}\mathbb{F}{% endequation %} שהוא הממשיים או המרוכבים, ועליו אנחנו מגדירים פונקציה {% equation %}\left\langle x,y\right\rangle :V\times V\to\mathbb{F}{% endequation %} שמקיימת לכל {% equation %}x,y{% endequation %}:

<ul> <li>{% equation %}\left\langle x_{1}+x_{2},y\right\rangle =\left\langle x_{1},y\right\rangle +\left\langle x_{2},y\right\rangle {% endequation %}</li>


<li>{% equation %}\left\langle \lambda x,y\right\rangle =\lambda\left\langle x,y\right\rangle {% endequation %}</li>


<li>{% equation %}\left\langle x,y\right\rangle =\overline{\left\langle y,x\right\rangle }{% endequation %}</li>


<li>{% equation %}\left\langle x,x\right\rangle \ge0{% endequation %} ושוויון מתקבל רק עבור {% equation %}x=0{% endequation %}</li>

</ul>

אחד מהדברים שאוהבים לעשות באלגברה לינארית <strong>בכל מקום אפשרי</strong> הוא לתרגם את השפה האבסטרקטית יחסית של "מרחבים" ו"טרנספורמציות" עליהם לשפה הקונקרטית בהרבה של <strong>מטריצות</strong>. הטריק הוא לבחור בסיס למרחב, ואז להסתכל לא על וקטורים אלא על <strong>הקואורדינטות</strong> שלהם, שהם איברים של {% equation %}\mathbb{F}^{n}{% endequation %} כש-{% equation %}n{% endequation %} הוא המימד של המרחב (אנחנו תמיד מניחים שהמרחב הוא ממימד סופי אחרת כל האלגברה הלינארית היא סיפור מסובך בהרבה) ולייצר טרנספורמציות לינאריות עם מטריצות. דיברתי על כל זה <a href="https://gadial.net/2011/10/27/coordinates_transformations_matrices/">כאן</a>, וזו הגישה שאאמץ מכאן ואילך.

ראשית, כשעוברים לדבר על וקטורים, קל לתאר את מה שנקרא "המכפלה הפנימית הסטנדרטית" שמוגדרת בתור {% equation %}\left\langle x,y\right\rangle =\sum_{i=1}^{n}x_{i}\overline{y}_{i}{% endequation %}. הרעיון הוא שאם {% equation %}x{% endequation %} הוא וקטור עמודה, וגם {% equation %}y{% endequation %} היא וקטור עמודה, אז {% equation %}y^{*}{% endequation %} (מה שמתקבל מ-{% equation %}y{% endequation %} על ידי שחלוף והצמדה) היא וקטור <strong>שורה</strong> ולכן הכפל {% equation %}y^{*}x{% endequation %} הולך להחזיר לנו סקלר בודד, שעל פי הגדרת כפל מטריצות יקיים בדיוק {% equation %}y^{*}x=\left\langle x,y\right\rangle {% endequation %}. אז ייצוג של המכפלה הפנימית הפשוטה ביותר בלשון איברים של {% equation %}\mathbb{F}^{n}{% endequation %} יש לנו.

מה עם מכפלות פנימיות מסובכות יותר? מה שמתברר למרבה השמחה הוא שאפשר לחשוב עליהן בתור משהו שהוא <strong>כמעט</strong> {% equation %}y^{*}x{% endequation %}, בהבדל שלא כופלים את {% equation %}y^{*}{% endequation %} ב-{% equation %}x{% endequation %} אלא בתוצאה של הפעלת <strong>טרנספורמציה לינארית</strong> על {% equation %}x{% endequation %}. כלומר לוקחים מטריצה {% equation %}A{% endequation %} ומסתכלים על הפונקציה {% equation %}f\left(x,y\right)=y^{*}Ax{% endequation %}. מה זה משיג לנו?

ובכן, היופי במושג הלא טריוויאלי של כפל מטריצות הוא האופן היפה שבו הוא תופס את תכונת <strong>הלינאריות</strong> של טרנספורמציות לינאריות. מתקיים:

{% equation %}A\left(x_{1}+x_{2}\right)=Ax_{1}+Ax_{2}{% endequation %}

{% equation %}A\left(\lambda x\right)=\lambda Ax{% endequation %}

משני אלו נקבל מיידית:

{% equation %}f\left(x_{1}+x_{2},y\right)=y^{*}A\left(x_{1}+x_{2}\right)=y^{*}Ax_{1}+y^{*}Ax_{2}=f\left(x_{1},y\right)+f\left(x_{2},y\right){% endequation %}

{% equation %}f\left(\lambda x,y\right)=y^{*}A\left(\lambda x\right)=\lambda y^{*}Ax=\lambda f\left(x,y\right){% endequation %}

כלומר - עצם השימוש במטריצה {% equation %}A{% endequation %} - <strong>כל מטריצה</strong> מסדר {% equation %}n\times n{% endequation %} - כבר נותן לי את שתי התכונות הראשונות של מכפלה פנימית. אבל מה הדרישות הנוספות שיתנו לי את שתי התכונות הבאות? אלו בדיוק הדרישות שיהפכו את {% equation %}A{% endequation %} מסתם מטריצה למה שאני קורא לו <strong>מטריצה חיובית לחלוטין</strong>.

ראשית, התכונה {% equation %}\left\langle x,y\right\rangle =\overline{\left\langle y,x\right\rangle }{% endequation %} ("הרמיטיות"). כשמנסחים את זה בלשון המטריציונית שלנו, זה אומר שצריך להתקיים

{% equation %}y^{*}Ax=\overline{\left(x^{*}Ay\right)}{% endequation %}

מכיוון שקצת קשה לראות איך להכניס את אופרטור ההצמדה פנימה, בואו נעבור לדבר על איברים בודדים. אם פותחים את הגדרות הכפל, {% equation %}y^{*}Ax{% endequation %} הוא הסקלר הבא:

{% equation %}y^{*}Ax=\sum_{j=1}^{n}\overline{y_{j}}\left(\sum_{i=1}^{n}A_{ij}x_{i}\right)=\sum_{i,j=1}^{n}A_{ij}x_{i}\overline{y_{j}}{% endequation %}

את <strong>זה</strong> קל להצמיד:

{% equation %}\overline{\sum_{i,j=1}^{n}A_{ij}x_{i}\overline{y_{j}}}=\sum_{i,j=1}^{n}\overline{A_{ij}}\overline{x_{i}}y_{j}=x^{*}A^{*}y{% endequation %}

ובאופן דומה, {% equation %}\overline{\left(x^{*}Ay\right)}=y^{*}A^{*}x{% endequation %}, כך שהשוויון למעלה מתורגם אל {% equation %}y^{*}Ax=y^{*}A^{*}x{% endequation %}. מכיוון שהוא נכון <strong>לכל</strong> {% equation %}x,y{% endequation %} הוא יהיה נכון בפרט עבור וקטורי יחידה, ומכך נקבל בסופו של דבר ש-{% equation %}A=A^{*}{% endequation %}. כלומר, כדי שתכונת ההרמיטיות תתקיים, אז {% equation %}A{% endequation %} צריכה להיות, אה, הרמיטית. או כמו שאני בדרך כלל קורא לזה, צמודה לעצמה.

זה משאיר אותנו עם התכונה האחרונה. אם {% equation %}x=0{% endequation %} אז {% equation %}x^{*}Ax=0{% endequation %} תמיד, לא משנה מה {% equation %}A{% endequation %}, כך שהתכונה שמעניינת אותנו היא שיתקיים {% equation %}x^{*}Ax>0{% endequation %} לכל {% equation %}x\ne0{% endequation %}. למטריצה צמודה לעצמה {% equation %}A{% endequation %} שמקיימת <strong>גם</strong> את התכונה הזו קוראים <strong>מטריצה חיובית לחלוטין </strong>(או "מוגדרת חיובית" או Positive Definite). אם מחלישים את הדרישה ורק דורשים {% equation %}x^{*}Ax\ge0{% endequation %} מקבלים את מה שנקרא <strong>מטריצה חיובית</strong> (או "מוגדרת אי שלילית" או Positve Semidefinite).

זו המוטיבציה להגדרה וההגדרה עצמה, אבל עכשיו בואו נראה כמה דרכים נוספות להסתכל על זה.

<h2>אפיונים שקולים של מטריצות חיוביות</h2>

ראשית, ערכים עצמיים. אנחנו כבר יודעים שאם {% equation %}A{% endequation %} היא מטריצה צמודה לעצמה, אז הערכים העצמיים שלה הם <strong>ממשיים</strong> (הראיתי את זה למשל <a href="https://gadial.net/2025/09/06/unitary_diagonalization/">כאן</a>), אבל אם היא חיובית אפשר לומר יותר מזה. נניח ש-{% equation %}Ax=\lambda x{% endequation %} עבור {% equation %}x\ne0{% endequation %}, אז {% equation %}x^{*}Ax=x^{*}\lambda x=\lambda\cdot\sum_{i=1}^{n}x_{i}\overline{x_{i}}=\lambda\cdot\sum\left|x_{i}\right|^{2}{% endequation %}

כלומר, {% equation %}x^{*}Ax{% endequation %} היא {% equation %}\lambda{% endequation %} כפול מספר חיובי כלשהו (הוא לא אפס כי {% equation %}x\ne0{% endequation %} אז לפחות אחד המחוברים יהיה גדול מאפס). הדרישה {% equation %}x^{*}Ax>0{% endequation %} מכתיבה שיתקיים גם {% equation %}\lambda>0{% endequation %}, כלומר <strong>הערכים העצמיים של מטריצה חיובית הם חיוביים</strong>. 

מה שנחמד הוא שגם הכיוון השני נכון - מטריצה צמודה לעצמה שכל הערכים העצמיים שלה הם חיוביים היא חיובית לחלוטין. במבט ראשון לא ברור לי איך להראות דבר כזה - ערכים עצמיים הם הרי דבר חמקמק, לכו תמצאו אותם, וגם כשמוצאים אותם לא בטוח שנמצא מספיק וקטורים עצמיים כדי לעשות עם זה משהו מעניין - אבל אני שוכח בזה שהנחתי שהמטריצה היא <strong>צמודה לעצמה</strong>. מרגע שמטריצה היא צמודה לעצמה, אז כמו<a href="https://gadial.net/2025/09/06/unitary_diagonalization/"> שהראיתי ממש לא מזמן</a>, היא ניתנת ללכסון אוניטרי. ולכסון אוניטרי הוא דבר חזק. זה אומר שאפשר לכתוב את {% equation %}A{% endequation %} בתור {% equation %}A=UDU^{*}{% endequation %} כך ש-{% equation %}D{% endequation %} אלכסונית ולכן כל הערכים העצמיים {% equation %}\left\{ \lambda_{1},\ldots,\lambda_{n}\right\} {% endequation %} כתובים בה יפה, ואילו {% equation %}U{% endequation %} הוא אוניטרית ({% equation %}UU^{*}=I{% endequation %}) כלומר העמודות שלה הן בסיס אורתונורמלי {% equation %}\left\{ v_{1},\ldots,v_{n}\right\} {% endequation %} של וקטורים עצמיים (את כל זה הסברתי בפוסט הקודם). אז מה שאפשר לעשות הוא לקחת וקטור {% equation %}x\ne0{% endequation %} <strong>כלשהו</strong> ולכתוב אותו בתור צירוף לינארי של הוקטורים העצמיים: {% equation %}x=\sum_{i=1}^{n}\alpha_{i}v_{i}{% endequation %}. לכן 

{% equation %}Ax=A\left(\sum_{i=1}^{n}\alpha_{i}v_{i}\right)=\sum_{i=1}^{n}\alpha_{i}Av_{i}=\sum_{i=1}^{n}\alpha_{i}\lambda_{i}v_{i}{% endequation %}

עכשיו, מה שמעניין אותנו הוא {% equation %}x^{*}Ax{% endequation %}, וכפי שאמרתי כבר, {% equation %}x^{*}Ax=\left\langle Ax,x\right\rangle {% endequation %} כשזו המכפלה הפנימית הסטנדרטית - וכשאני אומר שהעמודות של {% equation %}U{% endequation %} הן <strong>אורתונורמליות</strong> הכוונה היא ביחס למכפלה הפנימית הסטנדרטית, כלומר {% equation %}\left\langle v_{i},v_{j}\right\rangle =\delta_{ij}{% endequation %}. אז בואו נחשב!

{% equation %}x^{*}Ax=\left\langle Ax,x\right\rangle =\left\langle \sum_{i=1}^{n}\alpha_{i}\lambda_{i}v_{i},\sum_{j=1}^{n}\alpha_{i}v_{i}\right\rangle ={% endequation %}

{% equation %}=\sum_{i,j=1}^{n}\left\langle \alpha_{i}\lambda_{i}v_{i},\alpha_{j}v_{j}\right\rangle =\sum_{i,j=1}^{n}\lambda_{i}\alpha_{i}\overline{\alpha_{j}}\left\langle v_{i},v_{j}\right\rangle ={% endequation %}

{% equation %}=\sum_{i,j=1}^{n}\lambda_{i}\alpha_{i}\overline{\alpha_{j}}\delta_{ij}=\sum_{i=1}^{n}\lambda_{i}\left|\alpha_{i}\right|^{2}>0{% endequation %}

כשהמעבר האחרון נובע מכך שקיבלנו סכום שכל המחוברים בו הם מכפלה {% equation %}\lambda_{i}\left|\alpha_{i}\right|^{2}{% endequation %} של מספרים אי שליליים, {% equation %}\lambda_{i}>0{% endequation %} תמיד וקיים {% equation %}\alpha_{i}{% endequation %} כך ש-{% equation %}\left|\alpha_{i}\right|^{2}>0{% endequation %} כי {% equation %}x\ne0{% endequation %} (ולכן בצירוף הלינארי שנותן אותו לא כל המקדמים יכולים להיות 0). זה מסיים את ההוכחה! ושימו לב שאנחנו מקבלים באותה צורה משפט שאומר שמטריצה צמודה לעצמה שכל הערכים העצמיים שלה הם אי שליליים היא חיובית (לאו דווקא חיובית לחלוטין) פשוט כי במעבר האחרון נוכל להבטיח רק {% equation %}\ge0{% endequation %} ולא {% equation %}>0{% endequation %} (כי אמנם עדיין יש {% equation %}\left|\alpha_{i}\right|^{2}>0{% endequation %} אבל ייתכן שעבורו {% equation %}\lambda_{i}=0{% endequation %}).

בואו נעבור עכשיו לתכונה אפילו עוד יותר מלהיבה! ראשית, בואו נסתכל על משהו מההוכחה האחרונה - היו לי מכפלות מהצורה {% equation %}\alpha_{i}\overline{\alpha_{j}}{% endequation %} של מספר מרוכב והצמוד שלו, והן הפכו להיות {% equation %}\left|\alpha_{i}\right|^{2}{% endequation %} - כלומר מספר ממשי חיובי. זו תכונה מוכרת במספרים מרוכבים, ומה שמלהיב הוא שהיא עובדת גם עם מטריצות. אם ניקח מטריצה {% equation %}A{% endequation %} <strong>כלשהי</strong> ונסתכל על {% equation %}B=AA^{*}{% endequation %}, כלומר {% equation %}A{% endequation %} כפול הצמוד שלה, נקבל מטריצה {% equation %}B{% endequation %} שהיא חיובית.

ההוכחה היא די פשוטה: ראשית, צריך להוכיח ש-{% equation %}B{% endequation %} צמודה לעצמה אבל הרי {% equation %}B^{*}=\left(AA^{*}\right)^{*}=\left(A^{*}\right)^{*}A^{*}=AA^{*}=B{% endequation %}, אז את זה יש לנו. שנית, צריך להראות שלכל {% equation %}x{% endequation %} מתקיים {% equation %}x^{*}Bx\ge0{% endequation %}, ומתקיים {% equation %}x^{*}Bx=x^{*}AA^{*}x=\left(A^{*}x\right)^{*}A^{*}x=\left\langle A^{*}x,A^{*}x\right\rangle \ge0{% endequation %} כי מכפלה פנימית של איבר בעצמו היא תמיד אי-שלילית. יותר מכך - היא שווה אפס רק עבור אפס, כלומר רק אם {% equation %}A^{*}x=0{% endequation %}. עכשיו, בהחלט ייתכן ש-{% equation %}A^{*}x=0{% endequation %} אם {% equation %}x\ne0{% endequation %}, אבל אנחנו יודעים שדבר כזה קורה אם ורק אם {% equation %}A^{*}{% endequation %} <strong>סינגולרית</strong>, כלומר לא הפיכה. אנחנו גם יודעים ש-{% equation %}A^{*}{% endequation %} הפיכה אם ורק אם {% equation %}A{% endequation %} הפיכה. במילים אחרות, אם {% equation %}A{% endequation %} כן הפיכה אז {% equation %}AA^{*}{% endequation %} היא <strong>חיובית לחלוטין</strong>, מה שאנלוגי לכך ש-{% equation %}\alpha_{i}\overline{\alpha_{j}}>0{% endequation %} אלא אם {% equation %}\alpha_{i}=0{% endequation %} כלומר אם {% equation %}\alpha_{i}{% endequation %} הוא המספר המרוכב הלא-הפיך היחיד שקיים.

עוד יותר מעניין שגם הכיוון השני נכון: אם {% equation %}B{% endequation %} היא חיובית, אז אפשר לפרק אותה ל-{% equation %}B=AA^{*}{% endequation %}. כאן אנחנו צריכים כלי כבד יותר, שלמרבה המזל כבר יש לנו: מכיוון ש-{% equation %}B{% endequation %} חיובית היא צמודה לעצמה, ולכן ניתנת ללכסון אוניטרי, כלומר {% equation %}B=UDU^{*}{% endequation %} כאשר {% equation %}D{% endequation %} אלכסונית ו-{% equation %}U{% endequation %} אוניטרית. יותר מזה: האלכסון של {% equation %}B{% endequation %} כולל את הערכים העצמיים של {% equation %}B{% endequation %}, וכבר ראינו שהם כולם <strong>אי-שליליים</strong>, אז אפשר להוציא לכולם שורש, וזה מאפשר להוציא שורש ל-{% equation %}D{% endequation %} בעצמה.

בואו נראה את זה במפורש: נסמן

{% equation %}D=\left(\begin{array}{cccc} \lambda_{1}\\  & \lambda_{2}\\  &  & \ddots\\  &  &  & \lambda_{n} \end{array}\right){% endequation %} 

ואז נגדיר

{% equation %}\sqrt{D}=\left(\begin{array}{cccc} \sqrt{\lambda_{1}}\\  & \sqrt{\lambda_{2}}\\  &  & \ddots\\  &  &  & \sqrt{\lambda_{n}} \end{array}\right){% endequation %}

שימו לב: כאן לכתוב {% equation %}\sqrt{D}{% endequation %} זה סתם סימון, אבל השורשים שמופיעים על האיברים שעל האלכסון הם "אמיתיים", כלומר הפעלה של פונקציית השורש הרגילה על מספרים ממשיים אי-שליליים. הסימון הזה מוצדק כי כשכופלים שתי מטריצות אלכסוניות, מקבלים מטריצה אלכסונית שהאלכסון שלה הוא מכפלה איבר-איבר של האלכסונים של המטריצות המוכפלות. כלומר {% equation %}\sqrt{D}\cdot\sqrt{D}=D{% endequation %}. זה מאפשר לנו לכתוב:

{% equation %}B=U\sqrt{D}\sqrt{D}U^{*}{% endequation %}

עכשיו, {% equation %}\sqrt{D}{% endequation %} היא מטריצה שכל אבריה ממשיים והיא אלכסונית, כך ש-{% equation %}\sqrt{D}=\left(\sqrt{D}\right)^{*}{% endequation %}, אז קיבלנו

{% equation %}B=\left(U\sqrt{D}\right)\left(U\sqrt{D}\right)^{*}{% endequation %}

במילים אחרות, {% equation %}A=U\sqrt{D}{% endequation %} היא המטריצה שחיפשנו. עכשיו, אם {% equation %}B{% endequation %} לא הייתה סתם חיובית אלא חיובית לחלוטין, אז אין לה ערך עצמי 0, ולכן {% equation %}\sqrt{D}{% endequation %} היא מטריצה הפיכה, וכשמכפילים אותה ב-{% equation %}U{% endequation %} ההפיכה מקבלים מטריצה הפיכה - כך שהמסקנה היא שבפירוק {% equation %}B=AA^{*}{% endequation %}, נקבל ש-{% equation %}A{% endequation %} הפיכה אם ורק אם {% equation %}B{% endequation %} חיובית לחלוטין.

<h2>השורש החיובי של מטריצה חיובית</h2>

דבר אחד שצריך לשים לב אליו עם הפירוק שמצאנו עכשיו הוא שהפירוק הזה <strong>אינו יחיד</strong>, כי כשעושים לכסון אוניטרי יש הרבה דרכים לבנות את המטריצה {% equation %}U{% endequation %} - יש לנו את מרחב הוקטורים העצמיים, ואנחנו מוצאים לו בסיס אורתונורמלי ספציפי (ומסדרים אותו כך שהוקטורים העצמיים מתאימים לסדר שבו הערכים העצמיים מופיעים ב-{% equation %}D{% endequation %}). זה מתאים לאופן שבו אם אנחנו לוקחים מספר ממשי {% equation %}x\ge0{% endequation %}, יש הרבה מספרים מרוכבים {% equation %}z{% endequation %} כך ש-{% equation %}z\overline{z}=x{% endequation %}. מה שנכון הוא שקיים רק מספר יחיד {% equation %}y{% endequation %} כך ש-{% equation %}y\overline{y}=x{% endequation %} אם מגבילים את {% equation %}y{% endequation %} כך שיהיה ממשי אי-שלילי בעצמו: {% equation %}y\ge0{% endequation %}, ובמקרה הזה מכיוון ש-{% equation %}y{% endequation %} ממשי, {% equation %}\overline{y}=y{% endequation %} ולכן נקבל {% equation %}y^{2}=x{% endequation %}. ל-{% equation %}y{% endequation %} הזה יש סימון: {% equation %}\sqrt{x}{% endequation %}. במילים אחרות, אמרנו את הדבר הטריוויאלי שכולנו יודעים - למספר ממשי אי שלילי קיים ויחיד שורש אי שלילי.

העניין הוא שזה נכון גם למטריצות. אם {% equation %}B{% endequation %} חיובית, אז קיימת מטריצה {% equation %}\sqrt{B}{% endequation %} <strong>חיובית יחידה</strong> כך ש-{% equation %}\left(\sqrt{B}\right)^{2}=B{% endequation %}. בואו נוכיח את זה.

למצוא את {% equation %}\sqrt{B}{% endequation %} זה יחסית קל. ראינו קודם שאפשר לקחת לכסון אוניטרי {% equation %}B=UDU^{*}{% endequation %} ואז להגדיר {% equation %}A=U\sqrt{D}{% endequation %} ויתקיים {% equation %}AA^{*}=B{% endequation %}; בצורה הזו מקבלים שלל מטריצות שונות. אבל אפשר גם להגדיר {% equation %}A=U\sqrt{D}U^{*}{% endequation %}, ומה יקרה אז? נקבל

{% equation %}AA=\left(U\sqrt{D}U^{*}\right)\left(U\sqrt{D}U^{*}\right)=U\sqrt{D}\left(U^{*}U\right)\sqrt{D}U^{*}={% endequation %}

{% equation %}=U\sqrt{D}\sqrt{D}U^{*}=UDU^{*}=B{% endequation %}

אה-הא! קיבלנו שורש של {% equation %}B{% endequation %}! יותר מכך, אנחנו יודעים שיש לשורש הזה לכסון אוניטרי, הרי מזה התחלנו: {% equation %}U\sqrt{D}U^{*}{% endequation %}. מכיוון ש-{% equation %}\sqrt{D}{% endequation %} היא מטריצה אלכסונית עם מספרים ממשיים אי-שליליים על האלכסון אנחנו יודעים ש-{% equation %}A{% endequation %} היא צמודה לעצמה (אפשר גם פשוט לחשב את {% equation %}A^{*}{% endequation %} ולראות מה קורה) ושהיא חיובית. אז החלק של ה"קיום" היה קל. מה עם החלק של ה"יחידות"?

קודם, כשהגדרנו {% equation %}A=U\sqrt{D}{% endequation %}, המטריצה {% equation %}\sqrt{D}{% endequation %} הייתה קבועה אבל היה לנו חופש גדול לבחור את {% equation %}U{% endequation %} - זה היה בסיס אורתונורמלי כלשהו למרחב הוקטורים העצמיים של {% equation %}B{% endequation %}, עד כדי הסדר שבו אברי הבסיס מופיעים שכן נקבע על ידי {% equation %}D{% endequation %}. כאן לכאורה עדיין יש לנו חופש כזה כשמגדירים את {% equation %}A=U\sqrt{D}U^{*}{% endequation %} אלא שהפעם הכפל הנוסף ב-{% equation %}U^{*}{% endequation %} "מבטל" את החופש הזה - אנחנו תמיד נקבל את אותה מטריצה. אלא שזה נפנוף ידיים, לא נימוק רציני; ונימוק רציני צריך גם לטפל בשאלה המהותית יותר, האם יש דרכים <strong>אחרות</strong> לקבל שורש חיובי של {% equation %}B{% endequation %} שלא חשבנו עליהן. אז הנה הוכחה רצינית יותר, אבל גם מסובכת יותר.

האבחנה המרהיבה הראשונה היא שקיים פולינום {% equation %}p\in\mathbb{R}\left[x\right]{% endequation %} כך ש-{% equation %}p\left(B\right)=\sqrt{B}{% endequation %}. זה... מוזר, במבט ראשון. אנחנו חושבים על {% equation %}\sqrt{B}{% endequation %} בתור משהו שנמצא "נמוך יותר" מאשר {% equation %}B{% endequation %} במדד החזקות (הוא חזקת {% equation %}\frac{1}{2}{% endequation %}) בזמן שפולינום לוקח אותנו "גבוה יותר" (למשל, מעלה את {% equation %}B{% endequation %} בחזקת 2). אבל צריך לזכור שבמטריצות יש גבול כמה אפשר לעלות: <strong>הפולינום האופייני</strong> של מטריצה תמיד מאפס אותה (זה משפט קיילי המילטון שהראיתי <a href="https://gadial.net/2011/12/07/minimal_polynomial_and_cayley_hamillton/">כאן</a>) ואז אנחנו "מתחילים מהתחלה". עדיין, בואו נראה את הפלא קורה. ראשית, אני מסמן את הערכים העצמיים השונים של {% equation %}B{% endequation %} ב-{% equation %}\lambda_{1},\ldots,\lambda_{k}{% endequation %}. עכשיו, אפשר לבנות פולינום שמקיים {% equation %}p\left(\lambda_{i}\right)=\sqrt{\lambda_{i}}{% endequation %}, כלומר על המספרים שהם הערכים העצמיים של {% equation %}B{% endequation %} מחזיר את השורש שלהם (זה לא פולינום שמקודד את פונקציית השורש באופן כללי; רק על הערכים הספציפיים הללו). הדרך הסטנדרטית לעשות את זה היא באמצעות <strong>אינטרפולציית לגראנז'</strong> שנותנת לנו בניה מפורשת של הפולינום; במקרה הנוכחי

{% equation %}p\left(x\right)=\sum_{i=1}^{k}\prod_{j\ne i}\frac{x-\lambda_{j}}{\lambda_{i}-\lambda_{j}}\sqrt{\lambda_{i}}{% endequation %}

בתוך הפולינום הזה אפשר להציב <strong>מטריצות</strong>, כמו שקורה בקיילי המילטון. אם נציב את {% equation %}D{% endequation %}, אז מכיוון ש-{% equation %}D{% endequation %} אלכסונית ומטריצות אלכסוניות סגורות לכפל וחיבור, שמתורגמים לפעולות ישירות על האלכסון, בסך הכל יתקיים

{% equation %}p\left(D\right)=\left(\begin{array}{cccc} p\left(\lambda_{1}\right)\\  & p\left(\lambda_{2}\right)\\  &  & \ddots\\  &  &  & p\left(\lambda_{n}\right) \end{array}\right)=\left(\begin{array}{cccc} \sqrt{\lambda_{1}}\\  & \sqrt{\lambda_{2}}\\  &  & \ddots\\  &  &  & \sqrt{\lambda_{n}} \end{array}\right)=\sqrt{D}{% endequation %}

ועכשיו, אם נציב את {% equation %}UDU^{*}{% endequation %} ב-{% equation %}p{% endequation %} נקבל אפקט דומה: כי באופן כללי, {% equation %}UXU^{*}\cdot UYU^{*}=UXYU^{*}{% endequation %} ו-{% equation %}UXU^{*}+UYU^{*}=U\left(X+Y\right)U^{*}{% endequation %}, כלומר אפשר לעשות את החשבון תוך ששוכחים מה-{% equation %}U{% endequation %}-ים ולהחזיר אותם בסוף. אז 

{% equation %}p\left(UDU^{*}\right)=Up\left(D\right)U^{*}=U\sqrt{D}U^{*}=\sqrt{B}{% endequation %}.

לי אישית קשה להאמין בזה אז הנה דוגמת צעצוע כדי לשכנע את עצמי. ניקח מטריצה חיובית שהערכים העצמיים שלה הם 1,4,9 (כדי שהשורשים ייצאו נחמד), למשל {% equation %}B=\left(\begin{array}{ccc} 5 & 4 & 0\\ 4 & 5 & 0\\ 0 & 0 & 4 \end{array}\right){% endequation %} (שימו לב שהיא סימטרית והיא <strong>חייבת</strong> להיות סימטרית כדי להיות חיובית). עכשיו, אם מחשבים פולינום אינטרפולציה שמקיים {% equation %}p\left(1\right)=1,p\left(4\right)=2,p\left(9\right)=3{% endequation %} מקבלים את

{% equation %}p\left(x\right)=\frac{-x^{2}+25x+36}{60}{% endequation %}

זה בפני עצמו מרגיש לי קסם, שפולינום שנראה ככה עובד כל כך יפה (נסו להציב!) אבל זה היופי בפולינומים. עכשיו, חישוב ישיר יראה לנו ש-

{% equation %}B^{2}=\left(\begin{array}{ccc} 41 & 40 & 0\\ 40 & 41 & 0\\ 0 & 0 & 16 \end{array}\right){% endequation %}

ולכן:

{% equation %}60p\left(B\right)=-B^{2}+25B+36I=\left(\begin{array}{ccc} 120 & 60 & 0\\ 60 & 120 & 0\\ 0 & 0 & 120 \end{array}\right){% endequation %}

ולכן: {% equation %}A=\left(\begin{array}{ccc} 2 & 1 & 0\\ 1 & 2 & 0\\ 0 & 0 & 2 \end{array}\right){% endequation %}

ובאמת אם נחשב נקבל {% equation %}A^{2}=B{% endequation %}. קסם! יותר מזה, שימו לב שעשינו את הקסם הזה בלי להסתמך על אף {% equation %}U{% endequation %} בדרך; השתמשנו בפולינום האינטרפולציה {% equation %}p{% endequation %} שדרש רק את הידע על מהם הערכים העצמיים.

אוקיי, זה היה מלהיב ממש (עבורי) אבל איך זה מקדם אותנו להוכחה שהשורש הוא יחיד? ובכן, בואו נניח שיש <strong>עוד</strong> שורש, {% equation %}C{% endequation %}. כלומר, {% equation %}A^{2}=C^{2}=B{% endequation %}, וגם {% equation %}C{% endequation %} היא חיובית. אז מתקיים {% equation %}A=p\left(B\right)=p\left(C^{2}\right){% endequation %}, וזה אומר ש-{% equation %}A,C{% endequation %} הן <strong>מתחלפות בכפל</strong> כי אפשר לכתוב

{% equation %}AC=p\left(C^{2}\right)C=Cp\left(C^{2}\right)=CA{% endequation %}

כשההתחלפות באמצע נובעת מכך שכל מטריצה מתחלפת בכפל עם חזקות שלה. למה התחלפות זה מעניין? כי זה בדיוק מה שנדרש כדי ששתי מטריצות לכסינות יהיו <strong>לכסינות סימולטנית</strong>, מה שהראיתי <a href="https://gadial.net/2011/12/24/simultaneous_diagonalization/">כאן</a>. זה אומר שיש {% equation %}P{% endequation %} הפיכה ומטריצות אלכסוניות {% equation %}D_{1},D_{2}{% endequation %} כך ש-

{% equation %}A=PD_{1}P^{-1}{% endequation %}

{% equation %}C=PD_{2}P^{-1}{% endequation %}

ה"סימולטניות" מתבטאת בכך שזה אותו ה-{% equation %}P{% endequation %} לשתי המטריצות. אנחנו לא יודעים ש-{% equation %}D_{1}=D_{2}{% endequation %} אבל יהיה קל להוכיח את זה, כי {% equation %}A^{2}=B=C^{2}{% endequation %}, כלומר נקבל {% equation %}PD_{1}^{2}P^{-1}=PD_{2}^{2}P^{-1}{% endequation %} ומכאן ש-{% equation %}D_{1}^{2}=D_{2}^{2}{% endequation %}. בואו נראה מזה שהמטריצות המקוריות שוות.

המטריצות המקוריות הן אלכסוניות, אז מספיק להסתכל על מה שקורה לאיבר אחד על האלכסון, נאמר האיבר במקום ה-{% equation %}i{% endequation %}. אם נסתכל על הכניסה במקום ה-{% equation %}i{% endequation %} על האלכסון בשתי המטריצות, נראה שם שני ערכים {% equation %}\lambda_{1},\lambda_{2}{% endequation %}. אם עכשיו נעלה את שתי המטריצות בריבוע, הערכים הללו יהפכו להיות {% equation %}\lambda_{1}^{2},\lambda_{2}^{2}{% endequation %} והשוויון {% equation %}D_{1}^{2}=D_{2}^{2}{% endequation %} אומר לנו ש-{% equation %}\lambda_{1}^{2}=\lambda_{2}^{2}{% endequation %}. עכשיו, אם {% equation %}\lambda_{1},\lambda_{2}{% endequation %} היו מספרים מרוכבים כלליים, השוויון הזה לא היה אומר שהם זהים (כי למשל ייתכן ש-{% equation %}\lambda_{1}=-1,\lambda_{2}=1{% endequation %}) אבל אנחנו יודעים בדיוק מה יש ב-{% equation %}D_{1},D_{2}{% endequation %}; יש את השורשים של הערכים העצמיים של {% equation %}B{% endequation %}, כלומר מלכתחילה אלו היו מספרים ממשיים אי-שליליים, {% equation %}\lambda_{1},\lambda_{2}\ge0{% endequation %}, לכן גם הריבועים שלהם הם מספרים ממשיים אי שליליים, ולמספרים ממשיים אי-שליליים יש שורש יחיד שהוא ממשי אי-שלילי כך ש-{% equation %}\lambda_{1}=\lambda_{2}{% endequation %} וסיימנו את ההוכחה.

<h2>פירוק פולארי</h2>

עכשיו, אחרי שראינו כמה תוצאות נחמדות שקשורות למטריצות חיוביות ואולי גם קיבלנו אינטואיציה כלשהי למה שהולך פה, אני רוצה לשים אצבע טיפה יותר על הדמיון שיש בין מטריצות ומספרים כאן.

בואו ניזכר מה אנחנו יודעים על מרוכבים. כל מספר מרוכב {% equation %}z\in\mathbb{C}{% endequation %} הוא מהצורה {% equation %}z=a+bi{% endequation %} כאשר {% equation %}a,b\in\mathbb{R}{% endequation %}. זה נקרא <strong>ההצגה הקרטזית</strong> של המספר. <strong>הצמדה</strong> מוגדרת על ידי {% equation %}\overline{z}=a-bi{% endequation %}, כלומר זו הפעולה שמחליפה את {% equation %}i{% endequation %} ב-{% equation %}-i{% endequation %} (ומספר מרוכב {% equation %}z{% endequation %} הוא ממשי אם ורק אם {% equation %}z=\overline{z}{% endequation %}), ואפשר "לחלץ" את {% equation %}a,b{% endequation %} על ידי המשוואות {% equation %}a=\frac{z+\overline{z}}{2},b=\frac{z-\overline{z}}{2i}{% endequation %}. 

בנוסף, לכל מספר מרוכב יש גם <strong>הצגה פולרית</strong> ("קוטבית") מהצורה {% equation %}z=re^{i\theta}{% endequation %}. בזמן שבהצגה קרטזית, {% equation %}a,b{% endequation %} הם הקואורדינטות של {% equation %}z{% endequation %} במישור המרוכב, בהצגה הקוטבית {% equation %}r{% endequation %} מייצג את <strong>המרחק</strong> של {% equation %}z{% endequation %} מראשית הצירים ו-{% equation %}\theta{% endequation %} היא <strong>הזווית</strong> של הקו מראשית הצירים אל {% equation %}z{% endequation %}. המספר {% equation %}e^{i\theta}{% endequation %} הוא מספר מרוכב מערך מוחלט 1, בזמן ש-{% equation %}r\ge0{% endequation %} הוא מספר ממשי אי שלילי.

כל הרעיונות הללו עוברים הישר אל מטריצות, כאשר "מספר מרוכב" מוחלף על ידי "מטריצה", "מספר ממשי" מוחלף על ידי "מטריצה צמודה לעצמה", "מספר אי שלילי" מוחלף על ידי "מטריצה חיובית" ו"הצמדה" מוחלף על ידי "הצמדה" (כלומר הפעולה {% equation %}\overline{z}{% endequation %} מוחלפת על ידי הפעולה {% equation %}A^{*}{% endequation %}).

האנלוגיה די ברורה: אם {% equation %}A=A^{*}{% endequation %}, כלומר {% equation %}A{% endequation %} צמודה לעצמה, זה כמו {% equation %}z=\overline{z}{% endequation %} שמראה לנו ש-{% equation %}z{% endequation %} ממשי (אבל לאו דווקא חיובי). אפשר לייצג כל מטריצה {% equation %}M{% endequation %} בתור סכום {% equation %}M=A+B{% endequation %} כך ש-{% equation %}A{% endequation %} צמודה לעצמה ואילו {% equation %}B{% endequation %} היא <strong>אנטי</strong>-צמודה לעצמה, כלומר {% equation %}B^{*}=-B{% endequation %} (כמו ש-{% equation %}\overline{ib}=-ib{% endequation %}). אפשר "לחלץ" את {% equation %}A,B{% endequation %} עם המשוואות {% equation %}A=\frac{M+M^{*}}{2}{% endequation %} ו-{% equation %}B=\frac{M-M^{*}}{2}{% endequation %} (קל לראות ש-{% equation %}A^{*}=A{% endequation %}ו-{% equation %}B^{*}=-B{% endequation %}).

מה עם ההצגה הפולרית? ראינו קודם סיטואציה שבה היו לנו מטריצות מהצורה {% equation %}B=U\sqrt{D}{% endequation %}, כך ש-{% equation %}AA^{*}=B{% endequation %} עבור מטריצה חיובית {% equation %}B{% endequation %} מסוימת. זה בהחלט היה אנלוגי אל {% equation %}z=re^{i\theta}{% endequation %} שמקיים {% equation %}z\overline{z}=r^{2}{% endequation %}, כלומר איכשהו החלק של הסיבוב המרוכב נעלם. את המקום של {% equation %}r\ge0{% endequation %} הממשי החליפה המטריצה {% equation %}\sqrt{D}{% endequation %} ואילו את הסיבוב {% equation %}e^{i\theta}{% endequation %} החליפה המטריצה {% equation %}U{% endequation %}. הדמיון מובהק: {% equation %}e^{i\theta}{% endequation %} הוא מנורמה 1, ואילו {% equation %}U{% endequation %} היא אוניטרית, מה שתואם את האינטואיציה של "נורמה 1" כי כפל של {% equation %}U{% endequation %} באיבר כלשהו משמר את הנורמה שלו כמו שכפל ב-1 משמר את הגודל של מספר ממשי (אפשר לתת לזה משמעות יותר קונקרטית; יש נורמה שמגדירים על מטריצות על ידי {% equation %}\|A\|=\max_{x}\frac{\|Ax\|}{\|x\|}{% endequation %} ובהגדרה הזו הנורמה של מטריצה אוניטרית היא 1).

השאלה היא רק - האם זה קורה גם באופן כללי? האם לכל מטריצה {% equation %}A{% endequation %} יש "פירוק פולרי" {% equation %}A=UB{% endequation %} כך -{% equation %}U{% endequation %} אוניטרית ו-{% equation %}B{% endequation %} מטריצה חיובית? התשובה היא כן, אבל אני אחכה עם ההוכחה של זה לפוסט הבא. עדיין, אי אפשר לסיים בלי לפחות לומר מאיפה {% equation %}B{% endequation %} הזו מגיעה כי זה רק מחזק את האנלוגיה.

אם יש לנו מספר ממשי {% equation %}z{% endequation %} ואנחנו רוצים למצוא את הייצוג שלו בתור {% equation %}z=re^{i\theta}{% endequation %}, זה קל: {% equation %}r=\left|z\right|=\sqrt{a^{2}+b^{2}}{% endequation %}, ואז אפשר למצוא את {% equation %}e^{i\theta}=\frac{z}{r}{% endequation %} (בשביל למצוא את {% equation %}\theta{% endequation %} עצמה צריך להתאמץ עוד טיפה). עכשיו, {% equation %}\left|z\right|=\sqrt{z\cdot\overline{z}}{% endequation %}, ואת זה אפשר לקחת ישירות למטריצות: כבר ראינו שבהינתן מטריצה {% equation %}A{% endequation %} <strong>כלשהי</strong> מתקיים ש-{% equation %}AA^{*}{% endequation %} היא חיובית. ואם היא חיובית, אנחנו יודעים שיש לה שורש <strong>יחיד</strong> שהוא חיובי, כלומר קיימת מטריצה חיובית יחידה {% equation %}B{% endequation %} כך ש-{% equation %}B=\sqrt{AA^{*}}{% endequation %}. אבל האם אפשר לקבל עכשיו את {% equation %}U{% endequation %} פשוט על ידי "חילוק", {% equation %}U=AB^{-1}{% endequation %}? ובכן, לא - לא מובטח לנו ש-{% equation %}B{% endequation %} הפיכה בכלל. במקרה הזה אכן מה שיקרה הוא ש-{% equation %}U{% endequation %} לא תיקבע באופן יחיד. זה לא מקלקל לנו את האנלוגיה למספרים, כי עבור כל {% equation %}r>0{% endequation %} המקרה המקביל הוא מטריצה חיובית לחלוטין, והיא כן הפיכה; המקרה היחיד שתואם מטריצה חיובית שהיא לא חיובית לחלוטין הוא {% equation %}z=0{% endequation %} ובמקרה הזה באמת {% equation %}e^{i\theta}{% endequation %} לא נקבעת באופן יחיד בעצמה.

יש כמובן עוד הרבה מה לומר על הנושאים הללו אבל נראה לי שאעצור כאן, בפרט כי יש לי את כל מה שאני צריך בשביל הפוסט הבא. 