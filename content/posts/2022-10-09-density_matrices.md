---
title: "חישוב קוונטי: פורמליזם מטריצות הצפיפות"
layout: post
categories:
  - חישוב קוונטי
tags:
  - מטריצת צפיפות

description: "איך אפשר לתאר את המצב של מערכת קוונטית אם מדדו אותה אבל לא גילו לנו מה התוצאה? כאן נכנסת לתמונה דרך חדשה ומגניבה לתאר מערכות קוונטיות"
image: "2022/density_matrix.png"
---


<h2>מה זה מטריצות צפיפות ואיך מגיעים אליהן מוקטורי מצב?</h2>

בואו נדבר על סיטואציה פשוטה מאוד בחישוב קוונטי שכבר ראינו כמה פעמים בסדרת הפוסטים הזו: יש לנו את המצב הקוונטי על קיוביט בודד {% equation %}\left|+\right\rangle =\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}{% endequation %} ואנחנו מודדים אותו. מה קורה? קורים שני דברים: אנחנו, המודדים, מקבלים "החוצה" ביט של מידע - או 0 או 1 - והמצב הקוונטי עובר שינוי: אם ביט המידע שקיבלנו היה {% equation %}0{% endequation %} אז המצב הקוונטי הופך להיות {% equation %}\left|0\right\rangle {% endequation %}, ואם ביט המידע שקיבלנו היה 1 אז המצב הקוונטי הופך להיות {% equation %}\left|1\right\rangle {% endequation %}. כל אחת מהתוצאות הללו מתקבלת באותה הסתברות, כלומר {% equation %}\frac{1}{2}{% endequation %}.

טוב ויפה, אבל עכשיו נניח שאנחנו <strong>לא</strong> אלו שמודדים את המצב; אנחנו רואים מישהי אחרת באה ומודדת את המצב, ולא מגלה לנו מה התוצאה! מה אנחנו כן יכולים להגיד על המצב הנוכחי של הקיוביט? ובכן, בדיוק את מה שראינו לפני רגע: אנחנו יכולים לומר "בהסתברות {% equation %}\frac{1}{2}{% endequation %} הקיוביט במצב {% equation %}\left|0\right\rangle {% endequation %} ובהסתברות {% equation %}\frac{1}{2}{% endequation %} הקיוביט במצב {% equation %}\left|1\right\rangle {% endequation %}".

אחד הדברים המבלבלים והקשים ביותר להבנה כשמתחילים לדבר על חישוב קוונטי (ואולי על תורת הקוונטים בפרט?) הוא להבין שלומר "הקיוביט במצב {% equation %}\left|+\right\rangle {% endequation %}" זה <strong>ממש לא אותו דבר</strong> כמו לומר "בהסתברות {% equation %}\frac{1}{2}{% endequation %} הקיוביט במצב {% equation %}\left|0\right\rangle {% endequation %} ובהסתברות {% equation %}\frac{1}{2}{% endequation %} הקיוביט במצב {% equation %}\left|1\right\rangle {% endequation %}". הראשון הוא כמו לומר "החתול של שרדינגר בסופרפוזיציה של רגוע ועצבני" והשני הוא כמו לומר "החתול של שרדינגר רגוע או עצבני, אנחנו פשוט לא יודעים מי מהם כי עדיין לא פתחנו את הקופסה". עד סוף הפוסט, אולי אפילו עד האמצע שלו, כבר נראה את ה"ממש לא אותו דבר" הזה במלוא הפורמליזם המתמטי שלו - פורמליזם שעד כה טרם הצגתי, כי לא נזקקתי לו אבל אני רוצה להתחיל לדבר על דברים שמערבים אותו: פורמליזם <strong>מטריצת הצפיפות</strong>.

הרעיון במטריצת צפיפות הוא <strong>להכליל</strong> את האופן שבו אנחנו מתארים מצב של מערכת קוונטית. עד כה השתמשנו בוקטור כדי לתאר אותה: כך למשל {% equation %}\left|+\right\rangle {% endequation %} הוא הוקטור {% equation %}\frac{1}{\sqrt{2}}\left(\begin{array}{c} 1\\ 1 \end{array}\right){% endequation %}. בפורמליזם של מטריצות צפיפות, מה שמתאר את המצב של המערכת הקוונטית יהיה <strong>מטריצה</strong>: אם כדי לתאר מצב קוונטי על {% equation %}n{% endequation %} קיוביטים נזקקנו לוקטור מאורך {% equation %}2^{n}{% endequation %}, הרי שבשביל מטריצת צפיפות נזדקק למטריצה מסדר {% equation %}2^{n}\times2^{n}{% endequation %}. הגודל הנוסף הזה מאפשר לנו לכלול יותר מידע מאשר קודם; הוא מאפשר לנו בדיוק לתאר בצורה קומפקטית סיטואציה של "בהסתברות כך וכך המערכת נמצאת במצב כך וכך", עבור קבוצה של מצבים ולא רק עבור מצב בודד שאנחנו יודעים בודאות באיזה מצב הוא.

לפני שנגיע לפורמליזם, אני רוצה לחדד את הנקודה שאיתה פתחתי המצב {% equation %}\left|+\right\rangle {% endequation %} הוא מצב קוונטי ספציפי, קונקרטי. אין שום הסתברות שנלווית לתיאור הזה של המערכת. ההסתברות מתחילה לשחק תפקיד רק כאשר אנחנו מודדים את המצב, לא לפני כן. קל לראות את זה אם נזכרים שיש בעולם כמה דרכים שונות למדוד מצב קוונטי; מדידה "רגילה" היא מה שקראתי לו מדידה בבסיס {% equation %}Z{% endequation %}, מדידה שמתוארת על ידי האיברים {% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %} שהם התוצאות האפשריות של המדידה. אבל יש עוד מדידות, למשל מדידה בבסיס {% equation %}X{% endequation %} שמתוארת על ידי האיברים {% equation %}\left|+\right\rangle ,\left|-\right\rangle {% endequation %}. אם אני מבצע מדידה בבסיס {% equation %}X{% endequation %} של המצב {% equation %}\left|+\right\rangle {% endequation %}, אני אקבל את התוצאה שמתאימה ל-{% equation %}\left|+\right\rangle {% endequation %} בהסתברות של 100 אחוז.

לעומת זאת, אם המצב הקוונטי שלי הוא "בהסתברות {% equation %}\frac{1}{2}{% endequation %} הקיוביט במצב {% equation %}\left|0\right\rangle {% endequation %} ובהסתברות {% equation %}\frac{1}{2}{% endequation %} הקיוביט במצב {% equation %}\left|1\right\rangle {% endequation %}", מה יקרה אם אמדוד אותו בבסיס {% equation %}X{% endequation %}? אם הקיוביט במצב {% equation %}\left|0\right\rangle {% endequation %} אז בהסתברות {% equation %}\frac{1}{2}{% endequation %} נקבל {% equation %}\left|+\right\rangle {% endequation %} ובהסתברות {% equation %}\frac{1}{2}{% endequation %} נקבל {% equation %}\left|-\right\rangle {% endequation %}; ואם הקיוביט במצב {% equation %}\left|1\right\rangle {% endequation %} אז... במקרה הספציפי הזה של בסיס {% equation %}X{% endequation %}, יקרה בדיוק אותו דבר - כל תוצאה בהסתברות חצי (יכולים גם לקרות דברים מסובכים יותר באופן כללי).

אז כדי לחדד, אם המצב הקוונטי שלנו הוא {% equation %}\left|+\right\rangle {% endequation %} אז מדידה בבסיס {% equation %}X{% endequation %} תיתן בודאות מוחלטת {% equation %}\left|+\right\rangle {% endequation %}, אבל אם הוא "בהסתברות {% equation %}\frac{1}{2}{% endequation %} הקיוביט במצב {% equation %}\left|0\right\rangle {% endequation %} ובהסתברות {% equation %}\frac{1}{2}{% endequation %} הקיוביט במצב {% equation %}\left|1\right\rangle {% endequation %}" אז מדידה בסיס {% equation %}X{% endequation %} תיתן {% equation %}\left|+\right\rangle {% endequation %} רק בהסתברות {% equation %}\frac{1}{2}{% endequation %} ואחרת היא תיתן {% equation %}\left|-\right\rangle {% endequation %}. זה מראה לנו ששני המצבים הללו שונים, בודאות מוחלטת. וכאמור, להבין שהם שונים זה לטעמי אחד המכשולים הגדולים בדרך להבנה של חישוב קוונטי.

לפני שנעבור לדבר על מצבים קוונטיים מסובכים שמערבים הסתברויות, בואו ניקח צעד אחורה: ניזכר בפורמליזם המתמטי הרגיל של חישוב קוונטי באמצעות וקטורים, ונראה איך אפשר לבטא את כולו גם בשפה של מטריצות. אני חושב שזה ייראה די פשוט ולא קשה להבנה; יהיה קצת קשה להבין <strong>למה</strong> אנחנו עושים את זה אבל כבר הצהרתי מה המטרה שלנו פה.

אז הנה הפורמליזם: 

<ol> <li>מערכת קוונטית מתוארת על ידי מרחב הילברט {% equation %}\mathcal{H}{% endequation %} מעל {% equation %}\mathbb{C}{% endequation %}, ומצב ספציפי של המערכת הוא וקטור {% equation %}\left|\psi\right\rangle \in\mathcal{H}{% endequation %} מנורמה 1.</li>


<li>בהינתן אופרטור {% equation %}U:\mathcal{H}\to\mathcal{H}{% endequation %} שהוא <strong>אוניטרי</strong>, ניתן להפעיל אותו על המערכת על ידי כפל המטריצה שמייצגת את {% equation %}U{% endequation %} בוקטור שמייצג את מצב המערכת ולהעביר אותה למצב חדש: {% equation %}\left|\psi^{\prime}\right\rangle =U\left|\psi\right\rangle {% endequation %}.</li>


<li>בהינתן קבוצת אופרטורים {% equation %}\left\{ M_{0},M_{1},\ldots,M_{t}\right\} {% endequation %} שמכונים בהקשר הזה "אופרטורי מדידה", אפשר למדוד את המערכת ביחס לאופרטורים הללו ולקבל תוצאה {% equation %}i\in\left\{ 0,1,\ldots,t\right\} {% endequation %} בהסתברות {% equation %}p\left(i\right){% endequation %}, ואם התקבלה התוצאה הזו המערכת עוברת למצב {% equation %}\left|\psi^{i}\right\rangle {% endequation %}, כך ש: 

<ol>
<li>{% equation %}p\left(i\right)=\left\langle \psi\right|M_{i}^{\dagger}M_{i}\left|\psi\right\rangle {% endequation %}.</li>


<li>{% equation %}\left|\psi^{i}\right\rangle =\frac{M_{i}\left|\psi\right\rangle }{\sqrt{\left\langle \psi\right|M_{i}^{\dagger}M_{i}\left|\psi\right\rangle }}{% endequation %}.</li>
</ol>
</li>
</ol>

זה לא משהו קל לעיכול במיוחד אבל אני מניח שכבר ראינו את זה קודם - ואם לא, <a href="https://gadial.net/2022/07/28/quantum_computing_math/">הנה ההתחלה</a> של ה"קודם". בואו נראה עכשיו איך אותו דבר בדיוק מתואר עם מטריצה במקום וקטור.

ראשית, בואו ניזכר מה הסימונים שלנו אומרים. על {% equation %}\left|\psi\right\rangle {% endequation %} אני חושב בתור וקטור עמודה; במקרה הפשוט שבו {% equation %}\left|\psi\right\rangle {% endequation %} מייצג מערכת של קיוביט בודד, זה יהיה וקטור עמודה מסדר 2, {% equation %}\left|\psi\right\rangle =\left(\begin{array}{c} \alpha\\ \beta \end{array}\right){% endequation %}. בנוסף לכך, הצגתי סימון נוסף: {% equation %}\left\langle \psi\right|{% endequation %}. אפשר לחשוב על {% equation %}\left\langle \psi\right|{% endequation %} בתור {% equation %}\left\langle \psi\right|\triangleq\left(\left|\psi\right\rangle \right)^{\dagger}{% endequation %}, כלומר זה וקטור <strong>שורה </strong>{% equation %}\left\langle \psi\right|=\left(\begin{array}{cc} \overline{\alpha} & \overline{\beta}\end{array}\right){% endequation %}. יש עוד דרך לחשוב על {% equation %}\left\langle \psi\right|{% endequation %} בתור פונקציונל לינארי, אבל נעזוב את זה.

עכשיו, בסימון הזה, מה בעצם {% equation %}\left|\psi\right\rangle \left\langle \psi\right|{% endequation %} אומר? זו <strong>מטריצה</strong> מסדר {% equation %}2\times2{% endequation %} (ובאופן כללי, כש-{% equation %}\left|\psi\right\rangle {% endequation %} הוא וקטור מסדר {% equation %}n{% endequation %}, זו מטריצה {% equation %}n\times n{% endequation %}). כדי לראות את זה אני פשוט אכפול את הוקטורים במפורש:

{% equation %}\left|\psi\right\rangle \left\langle \psi\right|=\left(\begin{array}{c} \alpha\\ \beta \end{array}\right)\left(\begin{array}{cc} \overline{\alpha} & \overline{\beta}\end{array}\right)=\left(\begin{array}{cc} \left|\alpha\right|^{2} & \alpha\overline{\beta}\\ \overline{\alpha}\beta & \left|\beta\right|^{2} \end{array}\right){% endequation %}

זה פשוט על פי ההגדרה הרגילה של כפל מטריצות. שימו לב שאם אני כופל את שני הוקטורים הללו בסדר <strong>הפוך </strong>אני מקבל מטריצה מסדר {% equation %}1\times1{% endequation %} שאני חושב עליה בתור סקלר: 

{% equation %}\left\langle \psi\right|\left|\psi\right\rangle =\left(\begin{array}{cc} \overline{\alpha} & \overline{\beta}\end{array}\right)\left(\begin{array}{c} \alpha\\ \beta \end{array}\right)=\left|\alpha\right|^{2}+\left|\beta\right|^{2}{% endequation %}

בעצם, לכפול שני וקטורים בצורה הזו, {% equation %}\left\langle \psi\right|\left|\varphi\right\rangle {% endequation %}, נותן לנו את <strong>המכפלה הפנימית</strong> שלהם. על אותו משקל, לפעמים קוראים ל-{% equation %}\left|\psi\right\rangle \left\langle \varphi\right|{% endequation %} "מכפלה חיצונית" אבל נעזוב גם את זה. מה שמעניין, מבחינתי, זה רק איך שתרגממו את הוקטור {% equation %}\left|\psi\right\rangle {% endequation %} למטריצה {% equation %}\left|\psi\right\rangle \left\langle \psi\right|{% endequation %}. בשביל לקצר עניינים, אני אשתמש ב-{% equation %}\rho{% endequation %} בדרך כלל כדי לתאר מטריצות כאלו (כמו גם את המטריצות היותר מורכבות שנקבל בהמשך).

לפני שנסביר איך זה מסתדר עם המתמטיקה של התפתחות המערכת בזמן ושל מדידות, בואו נראה דוגמאות! קודם כל דוגמא פשוטה:

{% equation %}\left|0\right\rangle \left\langle 0\right|=\left(\begin{array}{c} 1\\ 0 \end{array}\right)\left(\begin{array}{cc} 1 & 0\end{array}\right)=\left(\begin{array}{cc} 1 & 0\\ 0 & 0 \end{array}\right){% endequation %}

ובאופן דומה:

{% equation %}\left|1\right\rangle \left\langle 1\right|=\left(\begin{array}{c} 0\\ 1 \end{array}\right)\left(\begin{array}{cc} 0 & 1\end{array}\right)=\left(\begin{array}{cc} 0 & 0\\ 0 & 1 \end{array}\right){% endequation %}

והנה ידידנו מתחילת הפוסט:

{% equation %}\left|+\right\rangle \left\langle +\right|=\frac{1}{\sqrt{2}}\left(\begin{array}{c} 1\\ 1 \end{array}\right)\frac{1}{\sqrt{2}}\left(\begin{array}{cc} 1 & 1\end{array}\right)=\left(\begin{array}{cc} \frac{1}{2} & \frac{1}{2}\\ \frac{1}{2} & \frac{1}{2} \end{array}\right){% endequation %}

והנה דוגמא דומה עם שני קיוביטים, עם מי שנקרא "מצב בל" (אחד מהם, ליתר דיוק): {% equation %}\left|\Phi^{+}\right\rangle =\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %}:

{% equation %}\left|\Phi^{+}\right\rangle \left\langle \Phi^{+}\right|=\frac{1}{\sqrt{2}}\left(\begin{array}{c} 1\\ 0\\ 0\\ 1 \end{array}\right)\frac{1}{\sqrt{2}}\left(\begin{array}{cccc} 1 & 0 & 0 & 1\end{array}\right)=\left(\begin{array}{cccc} \frac{1}{2} & 0 & 0 & \frac{1}{2}\\ 0 & 0 & 0 & 0\\ 0 & 0 & 0 & 0\\ \frac{1}{2} & 0 & 0 & \frac{1}{2} \end{array}\right){% endequation %}

הנה איור של מטריצת הצפיפות הזו; זה האופן שבו בדרך כלל מאיירים דברים כאלו (לפעמים עם איור נוסף, למקרה שהאיברים במטריצה הם מרוכבים):

<img src="{{site.baseurl}}{{site.post_images}}/2022/density_matrix.png" alt=""/>

אני מקווה שאלו מספיק דוגמאות כדי לקבל תחושה ראשונית ואפשר לעבור לתיאוריה המתמטית.

אם כדי לתאר את ההתפתחות של המערכת בהתאם לאופרטור {% equation %}U{% endequation %} היינו צריכים קודם לחשב מכפלה של מטריצה בוקטור, {% equation %}\left|\psi^{\prime}\right\rangle =U\left|\psi\right\rangle {% endequation %}, מה הנוסחה המתאימה כדי לחשב את {% equation %}\rho^{\prime}{% endequation %} מתוך {% equation %}\rho{% endequation %}? ובכן, אם נזכור ש-{% equation %}\left\langle \psi\right|=\left(\left|\psi\right\rangle \right)^{\dagger}{% endequation %}, אז נקבל ש-

{% equation %}\left\langle \psi^{\prime}\right|=\left(\left|\psi^{\prime}\right\rangle \right)^{\dagger}=\left(U\left|\psi\right\rangle \right)^{\dagger}=\left\langle \psi\right|U^{\dagger}{% endequation %}

(כי ככה אלו חוקי המטריצות: {% equation %}\left(AB\right)^{\dagger}=B^{\dagger}A^{\dagger}{% endequation %})

ומכאן:

{% equation %}\rho^{\prime}=\left|\psi^{\prime}\right\rangle \left\langle \psi^{\prime}\right|=U\left|\psi\right\rangle \left\langle \psi\right|U^{\dagger}=U\rho U^{\dagger}{% endequation %}

הפעולה, הזו של לקחת משהו ולכפול אותו מצד אחד ב-{% equation %}U{% endequation %} ומצד שני ב-{% equation %}U^{\dagger}{% endequation %} נקראת <strong>הצמדה</strong> והיא מאוד נפוצה במתמטיקה (בדרך כלל אמנם בגרסה שלה שבה ה-{% equation %}U^{\dagger}{% endequation %} הוא משמאל ולא מימין, אבל אין הבדל מהותי). אז בינתיים הכל נחמד - לקחנו פעולה טבעית בלשון וקטורים והחלפנו אותה בפעולה טבעית בלשון מטריצות.

עכשיו, נניח שאנחנו מודדים מצב {% equation %}\rho=\left|\psi\right\rangle \left\langle \psi\right|{% endequation %}, מה ההסתברות {% equation %}p\left(i\right){% endequation %} שאופרטור המדידה {% equation %}M_{i}{% endequation %} יעלה בגורל? אם נלך על פי הנוסחה {% equation %}p\left(i\right)=\left\langle \psi\right|M_{i}^{\dagger}M_{i}\left|\psi\right\rangle {% endequation %}, לא ברור מה יש לנו לעשות - איכשהו ה-{% equation %}\left\langle \psi\right|{% endequation %} וה-{% equation %}\left|\psi\right\rangle {% endequation %} מרוחקים מאוד זה מזה ולא ברור מה אפשר לעשות איתם... אלא אם כן אני אשלוף מהשרוול פיסת קסם של אלגברה לינארית.

זוכרים איך קיבלנו {% equation %}\left|\psi\right\rangle \left\langle \psi\right|=\left(\begin{array}{cc} \left|\alpha\right|^{2} & \alpha\overline{\beta}\\ \overline{\alpha}\beta & \left|\beta\right|^{2} \end{array}\right){% endequation %} ו-{% equation %}\left\langle \psi\right|\left|\psi\right\rangle =\left|\alpha\right|^{2}+\left|\beta\right|^{2}{% endequation %} וקראתי לראשון "מכפלה חיצונית" ולשני "מכפלה פנימית"? אם מסתכלים טיפה רואים שהמכפלה הפנימית מתחבאת בתוך {% equation %}\left|\psi\right\rangle \left\langle \psi\right|{% endequation %}: היא סכום אברי האלכסון הראשי של {% equation %}\left|\psi\right\rangle \left\langle \psi\right|{% endequation %}. "סכום אברי האלכסון הראשי" של מטריצה ריבועית {% equation %}A{% endequation %} הוא כזה דבר שימושי במתמטיקה שיש לו שם וסימן בפני עצמו; הוא נקרא <strong>העקבה</strong> של {% equation %}A{% endequation %} ומסומן {% equation %}\text{tr}\left(A\right)=\sum_{i=1}^{n}a_{ii}{% endequation %}, ומה שראינו עם המכפלה הפנימית והחיצונית הוא מקרה פרטי של הטענה הכללית הבאה באלגברה לינארית: אם {% equation %}A{% endequation %} היא מטריצה מסדר {% equation %}1\times n{% endequation %} ("וקטור שורה") ו-{% equation %}B{% endequation %} היא מטריצה מסדר {% equation %}n\times1{% endequation %} ("וקטור עמודה") אז 

{% equation %}AB=\text{tr}\left(BA\right){% endequation %}

ההוכחה של זה היא פשוט משחק באינדקסים:

{% equation %}\text{tr}\left(BA\right)=\sum_{i=1}^{n}\left[BA\right]_{ii}=\sum_{i=1}^{n}B_{i,1}A_{1,i}=AB{% endequation %}

איך זה עוזר לנו? ובכן, {% equation %}\left\langle \psi\right|{% endequation %} הוא וקטור שורה ואילו {% equation %}M_{i}^{\dagger}M_{i}\left|\psi\right\rangle {% endequation %} הוא וקטור עמודה, ולכן אפשר לבצע את החלפת המקומות הזו:

{% equation %}p\left(i\right)=\left\langle \psi\right|M_{i}^{\dagger}M_{i}\left|\psi\right\rangle =\text{tr}\left(M_{i}^{\dagger}M_{i}\left|\psi\right\rangle \left\langle \psi\right|\right)=\text{tr}\left(M_{i}^{\dagger}M_{i}\rho\right){% endequation %}

וקיבלנו גם כאן ניסוח נחמד של חישוב {% equation %}p\left(i\right){% endequation %} מתוך {% equation %}\rho{% endequation %} שמתבסס על מושגים מוכרים באלגברה לינארית.

אם אנחנו יודעים שהאופרטור {% equation %}M_{i}{% endequation %} עלה בגורל, אנחנו יודעים שהמצב הקוונטי עבר אל {% equation %}\left|\psi^{i}\right\rangle =\frac{M_{i}\left|\psi\right\rangle }{\sqrt{\left\langle \psi\right|M_{i}^{\dagger}M_{i}\left|\psi\right\rangle }}{% endequation %}. עם מה שכבר ראינו, אפשר לנסח את זה מחדש גם בלשון מטריצות:

{% equation %}\rho^{i}=\left|\psi^{i}\right\rangle \left\langle \psi^{i}\right|=\frac{M_{i}\left|\psi\right\rangle \left\langle \psi\right|M^{\dagger}}{\left(\sqrt{\left\langle \psi\right|M_{i}^{\dagger}M_{i}\left|\psi\right\rangle }\right)^{2}}=\frac{M_{i}\rho M_{i}^{\dagger}}{\text{tr}\left(M_{i}^{\dagger}M_{i}\rho\right)}{% endequation %}

וזה משלים את הניסוח מחדש של הסיטואציות שאנחנו כבר רגילים אליהן בלשון מטריצות במקום וקטורים, שזה נחמד אבל מן הסתם זו לא הפואנטה כי עם וקטורים זה נוח יותר. עכשיו אנחנו מגיעים אל הפואנטה - האופן שבו אפשר להשתמש בלשון מטריצות כדי לתאר סיטואציה הסתברותית "קלאסית" שמערבת מצבים קוונטיים. בזה אני מתכוון לכך שיש לנו מערכת קוונטית שיכולה להיות באחד מבין המצבים הקוונטיים {% equation %}\left|\psi_{1}\right\rangle ,\left|\psi_{2}\right\rangle ,\ldots,\left|\psi_{m}\right\rangle {% endequation %} אבל <strong>אנחנו לא יודעים איזה</strong>, אנחנו רק יודעים שהיא נמצאת במצב {% equation %}\left|\psi_{k}\right\rangle {% endequation %} בהסתברות {% equation %}p_{k}{% endequation %} שהיא מספר בין 0 ל-1: {% equation %}0\le p_{k}\le1{% endequation %}, כך ש-{% equation %}\sum_{k=1}^{m}p_{k}=1{% endequation %}. והאופן הפורמלי שבו אני הולך לתאר סיטואציה כזו הוא באמצעות המטריצה

{% equation %}\rho=\sum_{k=1}^{m}p_{k}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|{% endequation %}

ובמילים אחרות, אני לוקח את מטריצות הצפיפות של כל המצבים ולוקח את הממוצע המשוקלל שלהן, כשהמשקולות הן ההסתברויות של המצבים. כדאי כבר עכשיו להעיר שממטריצת הצפיפות שאני מקבל אני לא אוכל "לשחזר" את המצבים וההסתברויות שלהם; בהחלט אפשר יהיה לקבל את אותה מטריצת צפיפות מכמה סיטואציות שונות, אבל כל הסיטואציות הללו יהיו זהות מבחינת המשך ההתפתחות שלהן בזמן והתוצאות של מדידות אפשריות שלהן - כלומר, מטריצת הצפיפות היא דרך קומפקטית לשמור את המידע מבלי לאבד משהו מהותי.

בואו נבין למה שיטת הייצוג הזו באמת עובדת. נתחיל ממה קורה כשמפעילים אופרטור {% equation %}U{% endequation %} על המערכת. אם, בהסתברות {% equation %}p_{k}{% endequation %}, המערכת שלנו הייתה במצב {% equation %}\left|\psi_{k}\right\rangle {% endequation %}, אז אחרי הפעלת {% equation %}U{% endequation %} על המערכת אני מצפה להיות בהסתברות {% equation %}p_{k}{% endequation %} במצב {% equation %}U\left|\psi_{k}\right\rangle {% endequation %}, כלומר אני מצפה להיות ב-

{% equation %}\rho^{\prime}=\sum_{k=1}^{m}p_{k}U\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|U^{\dagger}=U\left(\sum_{k=1}^{m}p_{k}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|\right)U^{\dagger}=U\rho U^{\dagger}{% endequation %}

אז {% equation %}\rho{% endequation %}, גם כשהוא מייצג אוסף של מצבים קוונטיים, עדיין מתפתח כפי שציפינו על ידי הפעלת {% equation %}U{% endequation %}. 

כעת, מה אם מנסים למדוד את {% equation %}\rho{% endequation %} כשהוא מייצג אוסף? מה ההסתברות {% equation %}p\left(i\right){% endequation %} לקבל את התוצאה שמתאימה ל-{% equation %}M_{i}{% endequation %}? כמובן, זה תלוי באיזה מצב המערכת נמצאת. כבר ראינו שאם היא במצב {% equation %}\left|\psi_{k}\right\rangle {% endequation %}, ההסתברות לקבל את {% equation %}M_{i}{% endequation %} היא {% equation %}\text{tr}\left(M_{i}^{\dagger}M_{i}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|\right){% endequation %}. לכן:

{% equation %}p\left(i|k\right)=\text{tr}\left(M_{i}^{\dagger}M_{i}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|\right){% endequation %}

כאן אני משתמש בנוסחה להסתברות <strong>מותנית</strong>. בואו ניזכר שניה איך זה עובד באופן כללי: אם במרחב ההסתברות שלנו יש שני מאורעות, {% equation %}A,B{% endequation %}, אז

{% equation %}p\left(A|B\right)=\frac{p\left(A\cap B\right)}{p\left(B\right)}{% endequation %}

כאן אפשר לחשוב על מרחב ההסתברות שלנו כאילו הוא מתאר סדרה של שתי הגרלות: בהגרלה הראשונה נבחר מצב {% equation %}\left|\psi_{k}\right\rangle {% endequation %} באקראי, ובהגרלה השניה, שתלויה בראשונה, נבחר אופרטור מדידה {% equation %}M_{i}{% endequation %}. כלומר, מרחב ההסתברות שלנו כולל זוגות {% equation %}\left(k,i\right){% endequation %} של תוצאות אפשריות, והמאורע "{% equation %}\left|\psi_{k}\right\rangle {% endequation %} נבחר" הוא בעצם הקבוצה {% equation %}\left\{ \left(k,i\right)\ |\ 1\le i\le t\right\} {% endequation %} (כאן {% equation %}t{% endequation %} הוא מספר תוצאות המדידה האפשריות).

הסתברות מותנית מאפשרת לנו, כשאנחנו מנסים לחשב את ההסתברות של מאורע מסובך {% equation %}A{% endequation %}, לחלק את המרחב לפיסות נוחות לעיכול, {% equation %}B_{1},\ldots,B_{m}{% endequation %} שקל לחשב את {% equation %}p\left(A|B_{k}\right){% endequation %} לכל אחת מהן, ואז לחבר את כל הפיסות הללו כדי לקבל את {% equation %}p\left(A\right){% endequation %} המקורית. זה עובד כאשר מרחב ההסתברות שלנו הוא <strong>איחוד זר</strong> של כל ה-{% equation %}B_{k}{% endequation %}-ים הללו (כולם קבוצות זרות, והאיחוד שלהם נותן את כל מרחב ההסתברות). במקרה הזה מתקבל

{% equation %}p\left(A\right)=\sum_{k=1}^{m}p\left(A|B_{k}\right)p\left(B_{k}\right){% endequation %}

זה נקרא <strong>נוסחת ההסתברות השלמה</strong> וההוכחה פשוט מתבססת על כך ש-

{% equation %}\sum_{k=1}^{m}p\left(A|B_{k}\right)p\left(B_{k}\right)=\sum_{k=1}^{m}p\left(A\cap B_{k}\right)=p\left(A\cap\bigcup_{k=1}^{m}B_{k}\right)=p\left(A\right){% endequation %}

תוך שאנחנו משתמשים כאן באופן שבו הסתברות של איחוד מאורעות זרים הופכת לסכום ההסתברויות שלהם.

אם נחזור לענייננו, קיבלתי

{% equation %}p\left(i|k\right)=\text{tr}\left(M_{i}^{\dagger}M_{i}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|\right){% endequation %}

והמאורעות "{% equation %}\left|\psi_{k}\right\rangle {% endequation %} נבחר" הם בוודאי זרים, ולכן

{% equation %}p\left(i\right)=\sum_{k=1}^{m}p\left(i|k\right)p\left(k\right)=\sum_{k=1}^{m}p_{k}\text{tr}\left(M_{i}^{\dagger}M_{i}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|\right)={% endequation %}

{% equation %}=\text{tr}\left(M_{i}^{\dagger}M_{i}\sum_{k=1}^{m}p_{k}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|\right)=\text{tr}\left(M_{i}^{\dagger}M_{i}\rho\right){% endequation %}

כשהמעבר הלפני אחרון מתבסס על קסם אלגברה לינארית - שפונקציית העקבה {% equation %}\text{tr}{% endequation %} היא לינארית בעצמה (אפשר לראות את זה מחישוב ישיר).

גם פה -הגענו אל אותה נוסחה כמו קודם, רק שעכשיו היא תקפה גם למקרה של אוסף מצבים קוונטיים.

הדבר הבא שהראיתי היה לאן עוברים אחרי מדידה אם <strong>ידוע</strong> ש-{% equation %}M_{i}{% endequation %} עלה בגורל: המצב {% equation %}\left|\psi^{i}\right\rangle =\frac{M_{i}\left|\psi\right\rangle }{\sqrt{\left\langle \psi\right|M_{i}^{\dagger}M_{i}\left|\psi\right\rangle }}{% endequation %}. אם יש לנו אוסף של מצבים קוונטיים, אני מסמן ב-{% equation %}\left|\psi_{k}^{i}\right\rangle {% endequation %} את "המצב שאליו המערכת עוברת אם הייתה במצב {% equation %}\left|\psi_{k}\right\rangle {% endequation %} ואז עלתה בגורל תוצאת המדידה {% equation %}M_{i}{% endequation %}" (שימו לב שהמצבים הללו לא בהכרח שונים זה מזה, אבל זו לא בעיה, לא הייתה לי דרישה כזו). במילים אחרות, ההסתברות להיות ב-{% equation %}\left|\psi_{k}^{i}\right\rangle {% endequation %} היא {% equation %}p\left(i,k\right){% endequation %}. אבל השאלה שאני שואל כרגע היא מה ההסתברות להיות ב-{% equation %}\left|\psi_{k}^{i}\right\rangle {% endequation %} <strong>אם ידוע</strong> ש-{% equation %}M_{i}{% endequation %} עלה בגורל, כלומר "אם ידוע ש-{% equation %}M_{i}{% endequation %} עלה בגורל, מה ההסתברות שמלכתחילה היינו במצב {% equation %}\left|\psi_{k}\right\rangle {% endequation %}", כלומר {% equation %}p\left(k|i\right){% endequation %}, שהוא ההפך מ-{% equation %}p\left(i|k\right){% endequation %} שכבר חישבתי.

עכשיו, הנה טריק יעיל שנקרא "כלל בייס": מכיוון ש-{% equation %}p\left(A|B\right)=\frac{p\left(A\cap B\right)}{p\left(B\right)}{% endequation %} אפשר לכתוב {% equation %}p\left(A|B\right)p\left(B\right)=p\left(A\cap B\right){% endequation %}. אבל באותה צורה ממש מקבלים

{% equation %}p\left(B|A\right)p\left(A\right)=p\left(A\cap B\right)=p\left(A|B\right)p\left(B\right){% endequation %}

ולכן:

{% equation %}p\left(A|B\right)=\frac{p\left(B|A\right)p\left(A\right)}{p\left(B\right)}{% endequation %}

כלומר, זו שיטה להפוך את ההסתברות של א' שמותנה בקיום ב', להסתברות של ב' שמותנה בקיום א'. בפרט, בסיטואציות כמו הנוכחית שבה אנחנו חושבים על המאורעות בתור "מה שבא קודם" ו"מה שבא אחר כך", היא מאפשרת לעבור מהשאלה היותר אינטואיטיבית "בהינתן שקרה משהו, מה ההסתברות שינבע מכך משהו אחר בעתיד" אל השאלה הטריקית יותר "בהינתן שקרה משהו, מה ההסתברות שבעבר התרחש משהו שממנו זה נבע" (הסתברות א-פריורית אל מול הסתברות א-פוסטריורית).

עבורנו מה שמתקבל מכל זה כשאנחנו מתעסקים עם {% equation %}\rho=\sum_{k=1}^{m}p_{k}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|{% endequation %} הוא

{% equation %}p\left(k|i\right)=\frac{p\left(i|k\right)p\left(k\right)}{p\left(i\right)}=p_{k}\frac{\text{tr}\left(M_{i}^{\dagger}M_{i}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|\right)}{\text{tr}\left(M_{i}^{\dagger}M_{i}\rho\right)}{% endequation %}

עכשיו, המטרה שלי היא להבין לאן {% equation %}\rho{% endequation %} עברה אחרי המדידה בהינתן ש-{% equation %}M_{i}{% endequation %} עלה בגורל; מה התפלגות המצבים החדשה, כלומר מהו 

{% equation %}\rho^{i}=\sum_{k=1}^{m}p\left(k|i\right)\left|\psi_{k}^{i}\right\rangle \left\langle \psi_{k}^{i}\right|{% endequation %}

בואו נפשט את הנוסחה הזו. כזכור, {% equation %}\left|\psi_{k}^{i}\right\rangle =\frac{M_{i}\left|\psi_{k}\right\rangle }{\sqrt{\left\langle \psi_{k}\right|M_{i}^{\dagger}M_{i}\left|\psi_{k}\right\rangle }}{% endequation %} ולכן, כפי שכבר ראינו קודם,

{% equation %}\left|\psi_{k}^{i}\right\rangle \left\langle \psi_{k}^{i}\right|=\frac{M_{i}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|M_{i}^{\dagger}}{\text{tr}\left(M_{i}^{\dagger}M_{i}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|\right)}{% endequation %}

שימו לב שהמונה של {% equation %}p\left(k|i\right){% endequation %} והמכנה של {% equation %}\left|\psi_{k}^{i}\right\rangle \left\langle \psi_{k}^{i}\right|{% endequation %} מבטלים זה את זה! בזכות זה, אם נציב את שניהם בנוסחה {% equation %}\rho^{i}=\sum_{k=1}^{m}p\left(k|i\right)\left|\psi_{k}^{i}\right\rangle \left\langle \psi_{k}^{i}\right|{% endequation %}, נקבל

ואם נציב את מה שכבר מצאנו בנוסחה הזו, נקבל

{% equation %}\rho^{i}=\sum_{k=1}^{m}p_{k}\frac{M_{i}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|M_{i}^{\dagger}}{\text{tr}\left(M_{i}^{\dagger}M_{i}\rho\right)}=\frac{M_{i}\sum_{k=1}^{m}p_{k}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|M_{i}^{\dagger}}{\text{tr}\left(M_{i}^{\dagger}M_{i}\rho\right)}=\frac{M_{i}\rho M_{i}^{\dagger}}{\text{tr}\left(M_{i}^{\dagger}M_{i}\rho\right)}{% endequation %}

ושוב - קיבלנו את אותה נוסחה גם עבור מקבץ מצבים קוונטיים ולא מצב בודד. זה משלים את הכללת הפורמליזם של חישוב קוונטי מוקטורים שמייצגים מצב בודד, אל מטריצות צפיפות שמייצגות מקבץ של מצבים.

אבל לא סיימנו, עכשיו מגיע הקטע הכי נחמד! עד עכשיו תיארתי מה קורה עם מדידה שבה אנחנו מגרילים תוצאה ואז שואלים את עצמנו - בהינתן שקיבלנו את התוצאה {% equation %}M_{i}{% endequation %}, לאן עברנו? אבל עכשיו אפשר לדבר על השאלה - מה קורה אם אנחנו מבצעים מדידה ו<strong>לא יודעים</strong> מה התוצאה? זה מה שאיתו פתחנו.

אינטואיטיבית, מה שקורה במקרה הזה הוא שאנחנו עוברים לסיטואציה הסתברותית קלאסית: אם בהסתברות {% equation %}p\left(i\right){% endequation %} עברנו מהמקבץ {% equation %}\rho{% endequation %} אל המקבץ {% equation %}\rho^{i}{% endequation %}, אז עברנו אל מקבץ {% equation %}\rho^{\prime}{% endequation %} שמורכב מכל המקבצים {% equation %}\rho^{i}{% endequation %} הללו יחד, כשההסתברות של כל איבר במקבץ {% equation %}\rho^{i}{% endequation %} מוכפלת ב-{% equation %}p\left(i\right){% endequation %} (כי עכשיו יש לנו תהליך דו-שלבי לקבלת איבר במקבץ {% equation %}\rho^{\prime}{% endequation %}: ראשית מגרילים {% equation %}\rho^{i}{% endequation %} ואז מגרילים איבר מתוכו). כלומר

{% equation %}\rho^{\prime}=\sum_{i=1}^{t}p\left(i\right)\rho^{i}{% endequation %}

אבל כבר חישבנו את {% equation %}p\left(i\right),\rho^{i}{% endequation %}! נציב אותם בנוסחה ונקבל שוב ביטול הדדי נחמד:

{% equation %}\rho^{\prime}=\sum_{i=1}^{t}p\left(i\right)\rho^{i}=\sum_{i=1}^{t}\text{tr}\left(M_{i}^{\dagger}M_{i}\rho\right)\frac{M_{i}\rho M_{i}^{\dagger}}{\text{tr}\left(M_{i}^{\dagger}M_{i}\rho\right)}=\sum_{i=1}^{t}M_{i}\rho M_{i}^{\dagger}{% endequation %}

זו כנראה הנוסחה הפשוטה והיפה ביותר כאן, והיא הראשונה שבאמת מהווה משהו חדש - האופן שבו מערכת קוונטית מתפתחת בזמן תחת פעולת מדידה עם תוצאות לא ידועות. בואו נראה איך זה נותן לנו את הדוגמא מתחילת הפוסט.

את הפוסט התחלנו עם המצב {% equation %}\left|+\right\rangle {% endequation %}, שמתורגם למטריצת הצפיפות

{% equation %}\rho=\left|+\right\rangle \left\langle +\right|\frac{1}{\sqrt{2}}\left(\begin{array}{c} 1\\ 1 \end{array}\right)\frac{1}{\sqrt{2}}\left(\begin{array}{cc} 1 & 1\end{array}\right)=\left(\begin{array}{cc} \frac{1}{2} & \frac{1}{2}\\ \frac{1}{2} & \frac{1}{2} \end{array}\right){% endequation %}

אנחנו מודדים את {% equation %}\rho{% endequation %} בבסיס {% equation %}Z{% endequation %}, כלומר עם אופרטורי המדידה

{% equation %}M_{0}=\left(\begin{array}{cc} 1 & 0\\ 0 & 0 \end{array}\right),M_{1}=\left(\begin{array}{cc} 0 & 0\\ 0 & 1 \end{array}\right){% endequation %}

לאן {% equation %}\rho{% endequation %} יעבור אם אנחנו לא יודעים את תוצאת המדידה?

{% equation %}\rho^{\prime}=M_{0}\rho M_{0}^{\dagger}+M_{1}\rho M_{1}^{\dagger}={% endequation %}

{% equation %}=\left(\begin{array}{cc} 1 & 0\\ 0 & 0 \end{array}\right)\left(\begin{array}{cc} \frac{1}{2} & \frac{1}{2}\\ \frac{1}{2} & \frac{1}{2} \end{array}\right)\left(\begin{array}{cc} 1 & 0\\ 0 & 0 \end{array}\right)+\left(\begin{array}{cc} 0 & 0\\ 0 & 1 \end{array}\right)\left(\begin{array}{cc} \frac{1}{2} & \frac{1}{2}\\ \frac{1}{2} & \frac{1}{2} \end{array}\right)\left(\begin{array}{cc} 0 & 0\\ 0 & 1 \end{array}\right)={% endequation %}

{% equation %}=\left(\begin{array}{cc} \frac{1}{2} & 0\\ 0 & \frac{1}{2} \end{array}\right)=\frac{1}{2}\left(\begin{array}{cc} 1 & 0\\ 0 & 0 \end{array}\right)+\frac{1}{2}\left(\begin{array}{cc} 0 & 0\\ 0 & 1 \end{array}\right)=\frac{1}{2}\left|0\right\rangle \left\langle 0\right|+\frac{1}{2}\left|1\right\rangle \left\langle 1\right|{% endequation %}

והנה, קיבלנו באופן פורמלי את "בהסתברות {% equation %}\frac{1}{2}{% endequation %} הקיוביט במצב {% equation %}\left|0\right\rangle {% endequation %} ובהסתברות {% equation %}\frac{1}{2}{% endequation %} הקיוביט במצב {% equation %}\left|1\right\rangle {% endequation %}" וסגרנו מעגל עם תחילת הפוסט.

<h2>מה זה מטריצות צפיפות ואיך מגיעים אליהן בלי וקטורי מצב?</h2>

עד עכשיו הצגתי מטריצות צפיפות בתור הכללה של וקטורי מצב, אבל האם היה אפשר גם אחרת? האם בתיאוריה הייתי יכול להתחיל את התיאור של הפורמליזם המתמטי של חישוב קוונטי בלי לדבר על וקטורים בכלל, רק על מטריצות? התשובה היא "כן", אבל צריך להיות זהירים; כשם שלא כל וקטור הוא וקטור מצב, גם לא כל מטריצה היא מטריצת צפיפות.

ראשית, זוכרים איך וקטור {% equation %}\left|\psi\right\rangle {% endequation %} שהוא וקטור מצב חייב להיות מנורמה 1, כלומר לקיים {% equation %}\left\langle \psi\right|\left|\psi\right\rangle =1{% endequation %}? וזוכרים איך אפשר להחליף את הסדר בין המוכפלים אם משתמשים ב-tr? אז

{% equation %}\text{tr}\left(\left|\psi\right\rangle \left\langle \psi\right|\right)=\left\langle \psi\right|\left|\psi\right\rangle =1{% endequation %}

ועכשיו, עבור {% equation %}\rho=\sum_{k=1}^{m}p_{k}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|{% endequation %} כללי:

{% equation %}\text{tr}\left(\rho\right)=\text{tr}\left(\sum_{k=1}^{m}p_{k}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|\right)=\sum_{k=1}^{m}p_{k}\text{tr}\left(\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|\right)=\sum_{k=1}^{m}p_{k}=1{% endequation %}

כלומר, אם מטריצה {% equation %}\rho{% endequation %} רוצה להיות מטריצת צפיפות, ברור שהיא <strong>חייבת</strong> לקיים {% equation %}\text{tr}\left(\rho\right)=1{% endequation %}. אבל זה לא מספיק. יש עוד תכונה מהותית ש-{% equation %}\rho{% endequation %} מקיימת, ונובעת מהסימטריה של {% equation %}\left|\psi\right\rangle \left\langle \psi\right|{% endequation %}. אבל בשביל להבין מאיפה התכונה הזו מגיעה אולי שווה לתת טיפה רקע.

באלגברה לינארית הפעולה הבסיסית שמעניינת אותנו היא <strong>טרנספורמציה לינארית</strong>, פונקציה {% equation %}T:V\to W{% endequation %} שהיא לינארית, כלומר מקיימת {% equation %}T\left(u+v\right)=T\left(u\right)+T\left(v\right){% endequation %}, ו-{% equation %}T\left(\lambda v\right)=\lambda T\left(v\right){% endequation %}. זו תכונה כל כך יפה, שממנה נגזר שאפשר לתאר כל טרנספורמציה לינארית באמצעות הפעולה הפשוטה יחסית של כפל מטריצה בוקטור: קיימת מטריצה {% equation %}A_{T}{% endequation %} כך ש-{% equation %}T\left(v\right)=A_{T}\cdot v{% endequation %}.

אפשר לקחת את זה לשלב הבא ולדבר על העתקה <strong>בילינארית</strong>, שהיא פונקציה {% equation %}B:V\times U\to W{% endequation %} בשני משתנים שהיא לינארית בכל משתנה לחוד, כלומר

<ol> <li>{% equation %}B\left(v_{1}+v_{2},u\right)=B\left(v_{1},u\right)+B\left(v_{2},u\right){% endequation %}</li>


<li>{% equation %}B\left(v,u_{1}+u_{2}\right)=B\left(v,u_{1}\right)+B\left(v,u_{2}\right){% endequation %}</li>


<li>{% equation %}B\left(\lambda v,u\right)=\lambda B\left(v,u\right){% endequation %}</li>


<li>{% equation %}B\left(v,\lambda u\right)=\lambda B\left(v,u\right){% endequation %}</li>

</ol>

במקרה שבו {% equation %}V=U{% endequation %} ו-{% equation %}W=\mathbb{F}{% endequation %}, כלומר {% equation %}B{% endequation %} מעתיקה זוגות של איברים מ-{% equation %}V{% endequation %} אל איבר כלשהו בשדה ש-{% equation %}V{% endequation %} חי מעליו, קוראים ל-{% equation %}B{% endequation %} <strong>תבנית בילינארית</strong>, וכמו שאפשר לייצג פונקציה לינארית עם מטריצה, אפשר לייצג תבנית בילינארית עם מטריצה. ספציפית, קיימת מטריצה {% equation %}A{% endequation %} כך ש-

{% equation %}B\left(v,u\right)=v^{T}Au{% endequation %}

(אני מחפף פה ומניח שהוקטורים של {% equation %}V{% endequation %} הם מראש וקטורי עמודה; בפועל צריך לקחת בסיס ל-{% equation %}V{% endequation %} ואת וקטורי הקואורדינטות של {% equation %}v,u{% endequation %} אבל נעזוב את זה).

כשאנחנו מעל {% equation %}\mathbb{F}=\mathbb{R}{% endequation %}, אפשר לחשוב על <strong>מכפלה פנימית</strong> בתור מקרה פרטי מעניין של תבנית בילינארית. מעל המרוכבים זה טיפה יותר מסובך - אנחנו צריכים לדבר על משהו שנקרא <strong>תבנית הרמיטית</strong>, שמקיימת את תכונות 1-3 שהראיתי קודם, אבל 4 מוחלפת ב-{% equation %}B\left(v,\lambda u\right)=\overline{\lambda}B\left(v,u\right){% endequation %}, ובנוסף יש דרישה של מעין אנטי-סימטריות: {% equation %}B\left(u,v\right)=\overline{B\left(v,u\right)}{% endequation %}. מטריצה {% equation %}A{% endequation %} מייצגת את {% equation %}B{% endequation %} על ידי המשוואה הטיפה שונה

{% equation %}B\left(v,u\right)=v^{\dagger}A\overline{u}{% endequation %}

אבל כדי שתבנית הרמיטית תהיה מכפלה פנימית, על כל הדברים הנחמדים שנובעים מכך, יש עוד תכונה אחת שהיא חייבת לקיים: <strong>חיוביות</strong>. לכל {% equation %}v\ne0{% endequation %} צריך להתקיים

{% equation %}B\left(v,v\right)>0{% endequation %}

עכשיו, כשאנחנו חושבים על {% equation %}B{% endequation %} בתור משהו שמיוצג עם המטריצה {% equation %}A{% endequation %}, לאיזו דרישה על {% equation %}A{% endequation %} החיוביות מתורגמת? לכך שאם {% equation %}v\ne0{% endequation %} אז יתקיים

{% equation %}v^{T}A\overline{v}>0{% endequation %}

את הדרישה הזו אני יכול לנסח בצורה יותר נחמדה עבורנו אם אחליף את {% equation %}v{% endequation %} ב-{% equation %}\overline{v}{% endequation %} (זה לא משנה, כי אני עובר על כל ה-{% equation %}v\ne0{% endequation %}) ואקבל

{% equation %}v^{\dagger}Av>0{% endequation %}

מטריצה {% equation %}A{% endequation %} שמקיימת את התכונה הזו נקראת <strong>מטריצה חיובית</strong> (positive definite), וזו גם בדיוק התכונה שאני הולך לדרוש מ-{% equation %}\rho{% endequation %} שלנו שמתיימרת לייצג מצב קוונטי, בנוסף לדרישה שכבר ראינו ש-{% equation %}\text{tr}\left(\rho\right)=1{% endequation %}. בואו נבין למה זה מתקיים אם {% equation %}\rho{% endequation %} הגיעה מוקטורים, כלומר היא מהצורה

{% equation %}\rho=\sum_{k=1}^{m}p_{k}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|{% endequation %}

אנחנו לוקחים וקטור שונה מאפס כלשהו, {% equation %}v=\left|\varphi\right\rangle {% endequation %}, ומחשבים את {% equation %}v^{\dagger}\rho v{% endequation %}, כלומר את

{% equation %}\left\langle \varphi\right|\rho\left|\varphi\right\rangle {% endequation %}

עכשיו, עבור המקרה הפשוט שבו {% equation %}\rho=\left|\psi\right\rangle \left\langle \psi\right|{% endequation %} נקבל

{% equation %}\left\langle \varphi\right|\rho\left|\varphi\right\rangle =\left\langle \varphi\right|\left|\psi\right\rangle \left\langle \psi\right|\left|\varphi\right\rangle =\left|\left\langle \varphi,\psi\right\rangle \right|^{2}>0{% endequation %}

(כאשר כאן התוצאה התקבלה כי המכפלה הפנימית הרגילה מעל {% equation %}\mathbb{C}{% endequation %} היא חיובית)

ומכאן להכללה עבור סכום מהצורה {% equation %}\rho=\sum_{k=1}^{m}p_{k}\left|\psi_{k}\right\rangle \left\langle \psi_{k}\right|{% endequation %} הדרך טריוויאלית:

{% equation %}\left\langle \varphi\right|\rho\left|\varphi\right\rangle =\sum_{k=1}^{m}p_{k}\left|\left\langle \varphi,\psi_{k}\right\rangle \right|^{2}>0{% endequation %}

עכשיו אפשר לשכוח לחלוטין מוקטורי מצב ולנסח מחדש את עקרונות הבסיס של חישוב קוונטי בעזרת מטריצות צפיפות; אבל אני אעבור לדבר על <strong>אופרטור צפיפות</strong>, כי לדבר על מטריצה מניח במובלע בסיס (אין כזו הבדלה בשפה כשמדברים על וקטורים - המילה "וקטור" מתארת גם אובייקט כללי של מרחב וקטורי וגם את וקטור השורה שאיבריו הם אברי השדה, ולכן לא צצה הבחנה כזו קודם). מי שרגילות לאלגברה לינארית כבר יודעות שאת רוב מה שאפשר לומר על מטריצות, אפשר לומר על אופרטורים - פשוט לוקחים בסיס כלשהו ומוודאים שהמטריצה המייצגת של האופרטור בבסיס הזה מקיימת את התכונה הזו (מן הסתם זה דורש שהתכונה לא תהיה תלויה בבחירת הבסיס, ולמרבה המזל זה מה שקורה עם התכונות המעניינות באלגברה לינארית).

אם כן, בחישוב קוונטי אנחנו מתארים מערכת קוונטית מסויימת בעזרת מרחב הילברט {% equation %}\mathcal{H}{% endequation %}, כך שמצב המערכת בכל רגע נתון הוא אופרטור {% equation %}\rho:\mathcal{H}\to\mathcal{H}{% endequation %} שמקיים

<ul> <li>{% equation %}\text{tr}\left(\rho\right)=1{% endequation %}.</li>


<li>{% equation %}\rho{% endequation %} הוא אופרטור חיובי.</li>

</ul>

ואם המערכת נמצאת בהסתברות {% equation %}p_{k}{% endequation %} במצב {% equation %}\rho_{k}{% endequation %} אז המצב שלה הוא {% equation %}\rho=\sum_{k}p_{k}\rho_{k}{% endequation %}.

בהינתן אופרטור אוניטרי {% equation %}U:\mathcal{H}\to\mathcal{H}{% endequation %}, ניתן להפעיל אותו על המערכת כדי לשנות את מצבה:

{% equation %}\rho\mapsto U\rho U^{\dagger}{% endequation %}

ובהינתן אוסף של אופרטורי מדידה {% equation %}\left\{ M_{0},\ldots,M_{t}\right\} {% endequation %} מעל {% equation %}\mathcal{H}{% endequation %} שהדרישה היחידה עליהם היא שיתקיים {% equation %}\sum_{i=0}^{t}M_{i}^{\dagger}M_{i}=I{% endequation %}, ניתן למדוד את המערכת במצב {% equation %}\rho{% endequation %} ולקבל את התוצאה {% equation %}M_{i}{% endequation %} בהסתברות

{% equation %}p\left(i\right)=\text{tr}\left(M_{i}^{\dagger}M_{i}\rho\right){% endequation %}

ואם התקבלה תוצאה זו, המערכת עוברת למצב

{% equation %}\rho\mapsto\frac{M_{i}\rho M_{i}^{\dagger}}{\text{tr}\left(M_{i}^{\dagger}M_{i}\rho\right)}{% endequation %}

זה מסיים את ההגדרה, וכפי שראינו, תוצאה מיידית ממנה היא שאם מודדים את המערכת בעזרת {% equation %}\left\{ M_{0},\ldots,M_{t}\right\} {% endequation %} אבל תוצאת המדידה אינה ידועה לנו, המערכת עוברת מבחינתנו למצב 

{% equation %}\rho\mapsto\sum_{i=0}^{t}M_{i}\rho M_{i}^{\dagger}{% endequation %}

ייתכן מאוד שכבר שמתם לב שאם "מודדים" את המערכת באמצעות אופרטור מדידה בודד, {% equation %}\left\{ U\right\} {% endequation %}, שהוא אוניטרי, השינוי של המערכת עקב ה"מדידה" הזו הוא 

{% equation %}\rho\mapsto U\rho U^{\dagger}{% endequation %}

כלומר, השינוי ה"רגיל". של מצב המערכת. רק שעכשיו יש לנו קבוצה גדולה בהרבה של שינויים אפשריים, ואנחנו רוצים להבין אותה יותר טוב - למה? לא רק כי הם מייצגים מדידות, אלא גם כי הם מייצגים <strong>רעשים</strong>, שאפשר לחשוב עליהם בדיוק בתור "מדידות שלא אומרים לנו את התוצאה שלהן" ו"מדידות שמבוצעות באופן אקראי". בשביל לתאר את הדברים הללו אנחנו כבר חייבים את הפורמליזם של מטריצת הצפיפיות, מה שמצדיק את כל הפוסט הזה. אבל מה בדיוק מאפיין את קבוצת כל השינויים האפשריים הללו ואיך מייצגים איברים שלה? על זה נדבר בפוסט הבא. 
