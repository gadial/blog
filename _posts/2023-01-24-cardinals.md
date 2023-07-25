---
title: "תורת הקבוצות - עוצמות"
layout: post
categories:
  - תורת הקבוצות
tags:
  - עוצמות
image: "/assets/img/main/set_theory.png"
---


<h2>מבוא</h2>

אחד המושגים הבסיסיים בתורת הקבוצות הוא המושג של <strong>שקילות עוצמה</strong> של קבוצות; זו בעצם ההכללה של האמירה ששתי קבוצות הן "מאותו גודל" גם למקרה שבו הן אינסופיות. ההגדרה המתמטית, <a href="https://gadial.net/2020/10/09/what_are_infinite_sets/">שהראיתי בפוסט קודם</a>, הייתה יחסית פשוטה: אמרנו ש-{% equation %}A{% endequation %} שקולת עוצמה ל-{% equation %}B{% endequation %} וכתבנו {% equation %}\left|A\right|=\left|B\right|{% endequation %} (או {% equation %}A\sim B{% endequation %} אבל הפעם אני מעדיף את הסימון הראשון) אם קיימת פונקציה חד-חד-ערכית ועל {% equation %}f:A\to B{% endequation %}. קל לראות שעבור קבוצות סופיות שתי קבוצות הן שקולות עוצמה אם הן מאותו גודל, וגם היה קל יחסית לראות שעבור קבוצות אינסופיות יש מספר אינסופי של "גדלים" שונים: ראינו שלכל {% equation %}A{% endequation %} מתקיים {% equation %}\left|A\right|<\left|\mathcal{P}\left(A\right)\right|{% endequation %} (כאן {% equation %}\mathcal{P}\left(A\right){% endequation %} היא <strong>קבוצה החזקה</strong> של {% equation %}A{% endequation %} והסימון {% equation %}<{% endequation %} אומר שקיימת פונקציה חח"ע מהקבוצה השמאלית לימנית אבל <strong>לא קיימת</strong> פונקציה חח"ע ועל).

כל זה טוב ויפה, אבל בנוסף לזה ביצענו פשע מזעזע: אמרנו שקבוצה {% equation %}A{% endequation %} היא <strong>בת מניה</strong> אם {% equation %}\left|A\right|=\left|\mathbb{N}\right|{% endequation %}, וסימנו את זה על ידי {% equation %}\left|A\right|=\aleph_{0}{% endequation %}. וזה כבר פשוט מוזר. מה זה {% equation %}\aleph_{0}{% endequation %}? מי זה? אמרנו שזו <strong>העוצמה</strong> של {% equation %}A{% endequation %}, אבל <strong>מה זה</strong>? לא הסברנו. זה רק סימון? זה אובייקט? ואם זה {% equation %}\aleph_{0}{% endequation %} האם גם יש {% equation %}\aleph_{1}{% endequation %}? וכן הלאה. בפוסט הזה נסביר את הכל, והתשובה תהיה די פשוטה: עוצמה של קבוצה היא <strong>סודר</strong>; זו אחת הסיבות למה הצגתי אותם. אז בואו נעבור להגדרות הפורמליות.

<h2>מה זו עוצמה, פורמלית?</h2>

דרך אחת לדמיין עוצמה היא בתור <strong>מחלקת שקילות</strong>. מכיוון ששקילות עוצמות מקיימת רפלקסיביות, סימטריות וטרנזיטיביות, אפשר לומר שהיא יחס שקילות. אבל יחס שקילות <strong>על מה</strong>? על פניו, על אוסף כל הקבוצות, אבל אוסף כזה הוא גדול מכדי להיחשב "קבוצה" בעצמו - הוא מה שקוראים <strong>מחלקה</strong>, בעוד שיחס שקילות הוא תמיד תת-קבוצה של קבוצה.

ובכן, <a href="https://gadial.net/2023/01/18/classes_and_transfinite/">בפוסט הקודם</a> ראינו שהמתמטיקאים לא כל כך דוגמטיים בקטע הזה. אפשר לעבוד עם מחלקות, אפשר להגיד על מחלקה שהיא "פונקציה", ואפשר גם בצורה דומה להגדיר יחסי שקילות על מחלקות ולדבר על מחלקות שקילות. הבעיה היא שגם מחלקות השקילות הללו יהיו, ובכן, מחלקות במובן של "אוספים שאינם קבוצות", אבל יש טריק מרהיב למדי שמאפשר להגדיר "סוג של מחלקות שקילות" שהן כן קבוצות ולכן אובייקטים לגיטימיים בעולם, ו<strong>אפשר</strong> אם ממש רוצים להגדיר עוצמות בעזרתו - העוצמה של {% equation %}A{% endequation %} תהיה פשוט מחלקת השקילות המתאימה. 

אני הולך להראות את הגישה הזו בפוסט בעתיד, אבל היא <strong>לא</strong> מה שאני הולך להשתמש בו עכשיו; ההגדרה המקובלת יותר היא להגדיר עוצמה בתור סודר, וזה מה שנעשה כאן. החיסרון של השימוש בסודרים הוא שבהגדרה הזו, כדי שלכל קבוצה תהיה עוצמה מוגדרת, אנחנו נזקקים לאקסיומת הבחירה, ועוד רגע אסביר למה. השורה התחתונה של כל זה היא שבגלל שבתיאוריה יש יותר מהגדרה אפשרית אחת לעוצמה, אני אעבור להשתמש בשם אחר עבור המושג שאגדיר - <strong>מספר מונה</strong> (או בלועזית, מספר <strong>קרדינלי</strong>, Cardinal) ובקיצור, <strong>מונה</strong>, כמו שהגדרתי קודם <strong>סודר</strong>. 

אם כן, מונה הוא סוג מסויים של סודר: כזה שאינו שקול עוצמה לאף סודר שבא לפניו. פורמלית, סודר {% equation %}\alpha\in\text{Ord}{% endequation %} הוא מונה אם לכל {% equation %}\beta<\alpha{% endequation %} לא קיימת פונקציה חח"ע ועל {% equation %}f:\beta\to\alpha{% endequation %}. עכשיו אפשר להגדיר עוצמה של קבוצה כך: בהינתן קבוצה {% equation %}A{% endequation %} כלשהי, {% equation %}\left|A\right|{% endequation %} יהיה הסודר המינימלי במחלקת הסודרים שיש פונקציה חח"ע ועל מ-{% equation %}A{% endequation %} אליהם: 

{% equation %}\left|A\right|=\min\left\{ \alpha\in\text{Ord}\ |\ A\sim\alpha\right\} {% endequation %}

אלא שנשאלת השאלה - למה המחלקה הזו לא ריקה? האם תמיד קיים סודר ששקול ל-{% equation %}A{% endequation %}? ובכן, אם {% equation %}A{% endequation %} קבוצה סדורה היטב, בהחלט; קיים איזומורפיזם בין {% equation %}A{% endequation %} ובין הסודר שמייצג את טיפוס הסדר של הקבוצה הזו, ועבדנו קשה כדי להראות את זה. אבל אם {% equation %}A{% endequation %} לא סדורה היטב אנחנו בבעיה אמיתית. לכן אנחנו מגייסים לעזרתנו את אקסיומת הבחירה שמראה לנו שאפשר לסדר את {% equation %}A{% endequation %} בסדר טוב, ולכן קיים סודר כלשהו שיש התאמה חח"ע ועל בינו ובין {% equation %}A{% endequation %}, מה שהופך את ההגדרה של {% equation %}\left|A\right|{% endequation %} לתקינה. מכאן ואילך אשתמש בהגדרה הזו בצורה חופשית, אבל צריך לזכור שיש את אקסיומת הבחירה ברקע ואם נחליט לוותר עליה נצטרך להסביר מה נשמר ומה לא.

אוקיי, אז הגדרנו מונים, אבל <strong>מי הם</strong>? בתור התחלה, יש לנו את המונים הסופיים: {% equation %}0,1,2,\ldots{% endequation %}. זאת מכיוון שקבוצות סופיות הן שקולות עוצמה אם ורק אם יש בהן אותו מספר של איברים (צריך כמובן להוכיח את זה אבל עזבו אותי מזה כרגע). אחר כך יש לנו את {% equation %}\omega{% endequation %} שכמובן לא שקול עוצמה לאף סודר שקדם לו, כי כל מי שקודמים לו הם סופיים ולכן לא שקולים אליו (צריך כמובן להוכיח את זה אבל עזבו אותי מזה כרגע). 

כשאנחנו מדברים על {% equation %}\omega{% endequation %} בתור מונה ולא בתור סודר, אנחנו משתמשים בסימון אחר עבורו: {% equation %}\aleph_{0}{% endequation %}. למה בכלל לעשות הפרדה כזו? כי, למשל, עוד מעט נראה שיש עבור מונים כללי חיבור, כפל וחזקה, והכללים הללו <strong>שונים</strong> מהכללים עבור סודרים (למשל, חיבור וכפל הם כן קומוטטיביים) ולכן ההקשר פה הוא קריטי. גם הסימונים שבהם אשתמש כדי לתאר מונים "כלליים" יהיו שונים: {% equation %}\kappa,\lambda,\theta{% endequation %} וכאלו, להבדיל מה-{% equation %}\alpha,\beta,\gamma{% endequation %} ששימשו אותנו בהקשר של סודרים.

איזה עוד מונה אנחנו מכירים? האלכסון של קנטור מלמד אותנו ש-{% equation %}\left|\mathbb{N}\right|<\left|\mathbb{R}\right|{% endequation %} ולכן אנחנו מצפים שיהיה מונה שמתאים ל-{% equation %}\left|\mathbb{R}\right|{% endequation %} והוא יהיה גדול מ-{% equation %}\aleph_{0}{% endequation %}. אולי אפילו מפתה לקרוא לו {% equation %}\aleph_{1}{% endequation %}, אבל <strong>זהירות!</strong> זו לא ההגדרה של {% equation %}\aleph_{1}{% endequation %}. אז איך כן מסמנים את {% equation %}\left|\mathbb{R}\right|{% endequation %}? שאלה טובה. ראיתי לפעמים שמשתמשים ב-{% equation %}\aleph{% endequation %} (בלי אינדקס בכלל) אבל זה לא סימון רשמי במיוחד. אנחנו הולכים לראות עוד מעט סימון רשמי יותר, אבל בואו נבין מה זה ה-{% equation %}\aleph{% endequation %}-ים הללו בכללי.

בזכות משפט קנטור על קבוצת החזקה אנחנו יודעים שלכל {% equation %}A{% endequation %} קיימת קבוצה {% equation %}B{% endequation %} כך ש-{% equation %}\left|A\right|<\left|B\right|{% endequation %}. כלומר, לכל מונה {% equation %}\kappa{% endequation %} קיים מונה {% equation %}\lambda{% endequation %} כך ש-{% equation %}\kappa<\lambda{% endequation %} (יש גם הוכחה ישירה בלי אקסיומת הבחירה אם רוצים). אם כן, עבור {% equation %}\aleph_{0}{% endequation %} אפשר להסתכל על מחלקת המונים שגדולים ממנו ולקחת את האיבר המינימלי שלה ולקרוא לו {% equation %}\aleph_{1}{% endequation %} - זה המונה שבא "מייד אחרי" {% equation %}\aleph_{0}{% endequation %}. בדומה מוגדר {% equation %}\aleph_{n+1}{% endequation %} בתור המונה שבא מייד אחרי {% equation %}\aleph_{n}{% endequation %}, וקיבלנו סדרה אינסופית יפה של מונים:

{% equation %}\aleph_{0}<\aleph_{1}<\aleph_{2}<\ldots{% endequation %}

האם זה נגמר כאן? הו, לא ולא! בשביל מה הגדרנו סודרים אם לא כדי להגדיר באמצעותם סדרות ארוכות להחריד? אפשר ללכת לאינסוף ומעבר בעזרת ההגדרה

{% equation %}\aleph_{\omega}=\sup\left\{ \aleph_{0},\aleph_{1},\aleph_{2},\ldots\right\} {% endequation %}

מה זה סופרמום של קבוצת סודרים? הראינו כבר שאם לוקחים קבוצת סודרים ומאחדים את כל איבריה, מקבלים סודר חדש שגדול מכל האיברים בקבוצה הזו. מה שמעניין הוא שאם זו קבוצה של <strong>מונים</strong>, אז גם הסופרמום שיתקבל יהיה <strong>מונה</strong>, וזה כבר הרבה פחות מובן מאליו כי מונים הם סודרים "מיוחדים" שכאלו. אז בואו נוכיח את הטענה הכללית: אם {% equation %}A{% endequation %} היא קבוצה של מונים, אז {% equation %}\sup A{% endequation %} הוא מונה.

כדי להוכיח, נסמן {% equation %}\alpha=\sup A{% endequation %}. אני יודע ש-{% equation %}\alpha{% endequation %} הוא סודר, אבל אני צריך גם להראות שלכל סודר אחר {% equation %}\beta<\alpha{% endequation %} לא קיימת פונקציה חח"ע ועל בין {% equation %}\alpha{% endequation %} ו-{% equation %}\beta{% endequation %}; מספיק להראות שאם קיימת {% equation %}f:\alpha\to\beta{% endequation %} שהיא חח"ע אז מגיעים לסתירה. עכשיו, מכיוון ש-{% equation %}\alpha=\text{sup}A{% endequation %} הוא הסודר הקטן ביותר שגדול או שווה לכל אברי {% equation %}A{% endequation %}, מה שאומר בפרט ש-{% equation %}\beta{% endequation %} אינו כזה, ולכן קיים {% equation %}\kappa\in A{% endequation %} כך ש-{% equation %}\beta<\kappa\le\alpha{% endequation %}. מצד שני, מכיוון ש-{% equation %}\kappa{% endequation %} הוא מונה אז {% equation %}\kappa=\left|\kappa\right|{% endequation %}, ומכיוון ש-{% equation %}\kappa<\alpha{% endequation %} ו-{% equation %}\alpha{% endequation %} סודר אז {% equation %}\kappa\subseteq\alpha{% endequation %} ולכן אפשר לצמצם את {% equation %}f{% endequation %} אל {% equation %}\kappa{% endequation %} ולקבל פונקציה חח"ע {% equation %}f|_{\kappa}:\kappa\to\beta{% endequation %}. קיבלנו {% equation %}\left|\kappa\right|=\left|f|_{\kappa}\left(\kappa\right)\right|{% endequation %}, ומכיוון ש-{% equation %}f|_{\kappa}\left(\kappa\right)\subseteq\beta{% endequation %} אז {% equation %}\left|f|_{\kappa}\left(\kappa\right)\right|\le\left|\beta\right|{% endequation %}, אז בסך הכל קיבלנו את השרשרת

{% equation %}\kappa=\left|\kappa\right|=\left|f|_{\kappa}\left(\kappa\right)\right|\le\left|\beta\right|{% endequation %}

ומכך ש-{% equation %}\kappa\le\left|\beta\right|{% endequation %} אנחנו מקבלים בפרט {% equation %}\kappa\le\beta{% endequation %} (כי {% equation %}\kappa{% endequation %} קטן או שווה לסודר הראשון ששווה עוצמה ל-{% equation %}\beta{% endequation %}), בסתירה להנחה ש-{% equation %}\beta<\kappa{% endequation %}. זה מסיים את ההוכחה.

מה שטוב בהוכחה הזו הוא שהיא לא סתם מראה לנו ש-{% equation %}\aleph_{\omega}{% endequation %} היא מונה; היא מאפשרת לנו להראות ש<strong>לכל</strong> סודר {% equation %}\alpha{% endequation %} קיים מונה {% equation %}\aleph_{\alpha}{% endequation %} ששונה מקודמיו. ההגדרה של האלפים היא ברקורסיה על-סופית:

<ul> <li>{% equation %}\aleph_{0}=\omega{% endequation %}</li>


<li>{% equation %}\aleph_{\alpha+1}=\aleph_{\alpha}^{+}{% endequation %} לכל סודר {% equation %}\alpha{% endequation %} כאשר {% equation %}\aleph_{\alpha}^{+}{% endequation %} מסמן את המונה הקטן ביותר שגדול מ-{% equation %}\aleph_{\alpha}{% endequation %}.</li>


<li>{% equation %}\aleph_{\alpha}=\text{sup}\left\{ \aleph_{\beta}\ |\ \beta<\alpha\right\} {% endequation %} כאשר {% equation %}\alpha{% endequation %} הוא סודר גבולי.</li>

</ul>

האם כל המונים האינסופיים הם מהצורה {% equation %}\aleph_{\alpha}{% endequation %} עבור סודר {% equation %}\alpha{% endequation %} כלשהו? כן! בהינתן מונה {% equation %}\kappa{% endequation %} כלשהו, אפשר להסתכל על אוסף כל המונים שקטנים ממנו. האוסף הזה הוא תת-קבוצה של {% equation %}\kappa{% endequation %} עצמו (כי {% equation %}\kappa{% endequation %} הוא בפרט סודר ולכן כולל את כל הסודרים הקטנים ממנו) ולכן האוסף הזה הוא בעצמו קבוצה, ולא סתם קבוצה - קבוצה של סודרים, ולכן קבוצה שסדורה בסדר טוב, ולכן איזומורפית לסודר {% equation %}\alpha{% endequation %} כלשהו, וקיבלנו את ה-{% equation %}\aleph_{\alpha}{% endequation %} שאנחנו מחפשים, כי {% equation %}\left\{ \aleph_{\beta}\ |\ \beta<\alpha\right\} {% endequation %} זה בדיוק אוסף המונים שקטן מ-{% equation %}\kappa{% endequation %}.

יפה, הבנו מה זה סימון ה-{% equation %}\aleph{% endequation %} המוזר הזה, אבל מה עם {% equation %}\left|\mathbb{R}\right|{% endequation %}? אם זה לא {% equation %}\aleph_{1}{% endequation %}, מה זה כן? בשביל זה נצטרך לדבר קודם כל על <strong>חשבון עוצמות.</strong>

<h2>אריתמטיקה של עוצמות</h2>

מה שנחמד בחשבון עוצמות הוא שיש לנו הגדרה פשוטה לכל הפעולות בלשון של קבוצות, מה שלא קרה בסודרים (שם נזקקנו להגדרה רקורסיבית). נתחיל מהמקרה שבו {% equation %}A,B{% endequation %} הן קבוצות סופיות, ואז אנחנו ממש יכולים להוכיח שמתקיים:

<ul> <li>{% equation %}\left|A\right|+\left|B\right|=\left|A\cup B\right|{% endequation %} (בהינתן {% equation %}A\cap B=\emptyset{% endequation %})</li>


<li>{% equation %}\left|A\right|\cdot\left|B\right|=\left|A\times B\right|{% endequation %}</li>


<li>{% equation %}\left|A\right|^{\left|B\right|}=\left|A^{B}\right|{% endequation %}</li>

</ul>

כמובן, בשביל להבין מה הולך פה צריך להכיר את הפעולות על הקבוצות עצמן. אז בואו נזכיר אותן.

ראשית יש לנו איחוד: {% equation %}A\cup B{% endequation %} היא הקבוצה שכוללת את כל האיברים של {% equation %}A{% endequation %} ואת כל האיברים של {% equation %}B{% endequation %}. מן הסתם נצפה שהגודל שלה יהיה שווה לסכום הגדלים של {% equation %}A{% endequation %} ושל {% equation %}B{% endequation %}, אבל יש כאן עניין טריקי אחד: אם יש ל-{% equation %}A,B{% endequation %} איברים משותפים, אז האיברים המשותפים הללו אמורים להיספר רק פעם אחת (אין כפילויות בתוך קבוצה). לכן הנוסחה הנכונה באופן כללי עבור קבוצות סופיות היא {% equation %}\left|A\cup B\right|=\left|A\right|+\left|B\right|-\left|A\cap B\right|{% endequation %}, שמחסרת את מספר האיברים שנספרו פעמיים. יש לזה גם הכללה מאוד יפה למספר גדול יותר של קבוצות שנקראת <strong>עקרון ההכלה וההפרדה</strong> אבל <a href="https://gadial.net/2011/12/31/inclusion_exclusion_principle/">זה באמת לפוסט אחר</a>. כשאנחנו באים להגדיר חיבור, אנחנו פשוט מניחים שהקבוצות זרות, ללא איברים משותפים; תמיד אפשר להשיג את האפקט הזה על ידי שינוי שמות האיברים באחת הקבוצות, אם צריך (יש ממש פעולה שנקראת <strong>איחוד זר</strong> שמבצעת את שינוי השמות הזה על הדרך, אבל אין טעם להיכנס לרמת הפורמליסטיקה הזו).

עבור כפל אנחנו מסתמכים על מושג המכפלה הקרטזית של קבוצות, {% equation %}A\times B=\left\{ \left(a,b\right)\ |\ a\in A,b\in B\right\} {% endequation %}. למה זה יוצא כפל? כי לכל איבר {% equation %}a\in A{% endequation %}, קיימים {% equation %}\left|B\right|{% endequation %} זוגות מהצורה {% equation %}\left(a,b\right){% endequation %} כש-{% equation %}b\in b{% endequation %}; ויש {% equation %}\left|A\right|{% endequation %} ערכים אפשריים של {% equation %}A{% endequation %} שעבורם יהיו {% equation %}\left|B\right|{% endequation %} זוגות כאלו - בסך הכל {% equation %}\left|A\right|\times\left|B\right|{% endequation %}, קל למדי.

ועבור חזקה? כזכור, השימוש {% equation %}A^{B}{% endequation %} משמש אותנו להגדרת קבוצת הפונקציות מ-{% equation %}B{% endequation %} אל {% equation %}A{% endequation %} (לאו דווקא פונקציות חח"ע/על; כל פונקציה). אם {% equation %}A,B{% endequation %} קבוצות סופיות, אז קל לספור כמה פונקציות כאלו יש: כל פונקציה כזו צריכה לבצע {% equation %}\left|B\right|{% endequation %} בחירות, אחת לכל איבר של {% equation %}B{% endequation %} , לאן היא רוצה להעביר אותו. יש לנו {% equation %}\left|A\right|{% endequation %} אפשרויות לכל בחירה כזו, כלומר מספר האפשרויות הכולל הוא {% equation %}\left|A\right|\cdot\left|A\right|\cdots\left|A\right|{% endequation %} בדיוק {% equation %}\left|B\right|{% endequation %} פעמים, ולכן בסך הכל {% equation %}\left|A\right|^{\left|B\right|}{% endequation %}. זה מסביר גם את מה שנראה כמו "היפוך" שבו {% equation %}A^{B}{% endequation %} הוא פונקציות מ-{% equation %}B{% endequation %} אל {% equation %}A{% endequation %} ולא ההפך; זה מה שמסתדר לנו עם התוצאה המספרית המתמטית.

יופי, אז הוכחנו את הטענות על הגדלים של קבוצות סופיות - זה ממש הבסיס של התחום שנקרא <strong>קומבינטוריקה</strong>. אבל אנחנו פה כדי לדבר על קבוצות אינסופיות, אז אנחנו רוצים להפוך את התוצאות שלעיל להגדרות של ממש, עבור כל זוג מספרים מונים {% equation %}\kappa,\lambda{% endequation %}.

זה הולך ככה:

<ul> <li>{% equation %}\kappa+\lambda\triangleq\left|A\cup B\right|{% endequation %} עבור קבוצות {% equation %}A,B{% endequation %} כך ש-{% equation %}\left|A\right|=\kappa,\left|B\right|=\lambda{% endequation %} ו-{% equation %}A\cap B=\emptyset{% endequation %}</li>


<li>{% equation %}\kappa\cdot\lambda\triangleq\left|A\times B\right|{% endequation %} עבור קבוצות {% equation %}A,B{% endequation %} כך ש-{% equation %}\left|A\right|=\kappa,\left|B\right|=\lambda{% endequation %}</li>


<li>{% equation %}\kappa^{\lambda}\triangleq\left|A^{B}\right|{% endequation %} עבור קבוצות {% equation %}A,B{% endequation %} כך ש-{% equation %}\left|A\right|=\kappa,\left|B\right|=\lambda{% endequation %}</li>

</ul>

ההגדרה הזו טיפה בעייתית כי היא מסתמכת על <strong>בחירת נציגים</strong> עבור {% equation %}\kappa,\lambda{% endequation %}, וצריך להוכיח שלמרות זאת הכל <strong>מוגדר היטב</strong>. כלומר, שאם ניקח {% equation %}A^{\prime},B^{\prime}{% endequation %} כך ש-{% equation %}\left|A^{\prime}\right|=\kappa,\left|B^{\prime}\right|=\lambda{% endequation %} אז נקבל ש-{% equation %}\left|A\cup B\right|=\left|A^{\prime}\cup B^{\prime}\right|{% endequation %} (אם גם הקבוצות החדשות זרות) ו-{% equation %}\left|A\times B\right|=\left|A^{\prime}\times B^{\prime}\right|{% endequation %} ו-{% equation %}\left|A^{B}\right|=\left|\left(A^{\prime}\right)^{B^{\prime}}\right|{% endequation %}. 

אלו הוכחות סטנדרטיות אבל בואו נבין את הרעיון עבור המקרה של {% equation %}\left|A\times B\right|=\left|A^{\prime}\times B^{\prime}\right|{% endequation %}: אם {% equation %}\left|A\right|=\kappa=\left|A^{\prime}\right|{% endequation %} אז בפרט קיימת פונקציה {% equation %}f_{A}:A\to A^{\prime}{% endequation %} שהיא חח"ע ועל, ובדומה קיימת {% equation %}f_{B}:B\to B^{\prime}{% endequation %} חח"ע ועל. עכשיו נגדיר {% equation %}g:A\times B\to A^{\prime}\times B^{\prime}{% endequation %} בדרך ה"טבעית": {% equation %}g\left(\left(a,b\right)\right)=\left(f_{A}\left(a\right),f_{B}\left(b\right)\right){% endequation %}. זו פונקציה חח"ע כי אם {% equation %}g\left(\left(a,b\right)\right)=g\left(\left(x,y\right)\right){% endequation %} אז {% equation %}\left(f_{A}\left(a\right),f_{B}\left(b\right)\right)=\left(f_{A}\left(x\right),f_{B}\left(y\right)\right){% endequation %} ומהגדרת מכפלה קרטזית נקבל שוויון רכיב-רכיב, כלומר {% equation %}f_{A}\left(a\right)=f_{A}\left(x\right){% endequation %} ומכך ש-{% equation %}f_{A}{% endequation %} חח"ע נקבל {% equation %}a=x{% endequation %} ובאופן דומה נקבל {% equation %}b=y{% endequation %} ולכן {% equation %}\left(a,b\right)=\left(x,y\right){% endequation %}. בנוסף, {% equation %}g{% endequation %} גם על כי אם {% equation %}\left(x,y\right)\in A^{\prime}\times B^{\prime}{% endequation %} אז מהגדרת מכפלה קרטזית {% equation %}x\in A^{\prime}{% endequation %} ומכיוון ש-{% equation %}f_{A}{% endequation %} על קיים {% equation %}a\in A{% endequation %} כך ש-{% equation %}f_{A}\left(a\right)=x{% endequation %} ובדומה קיים {% equation %}b\in B{% endequation %} כך ש-{% equation %}f_{B}\left(b\right)=y{% endequation %} ולכן {% equation %}g\left(\left(a,b\right)\right)=\left(f_{A}\left(a\right),f_{B}\left(b\right)\right)=\left(x,y\right){% endequation %}.

בקיצור, קל להראות שבחירת הנציגים לא משפיעה, גם בלי להזדקק במיוחד לאקסיומת הבחירה או משהו דומה. זה מאפשר לנו לעבור בלב שקט להוכחה של <strong>תכונות</strong> האריתמטיקה של עוצמות (אני משתמש בחופשיות בסימן {% equation %}\cdot{% endequation %} לכפל ולפעמים משמיט אותו):

<ul> <li>{% equation %}\kappa+\lambda=\lambda+\kappa{% endequation %} וגם {% equation %}\kappa\cdot\lambda=\lambda\cdot\kappa{% endequation %} (קומוטטיביות)</li>


<li>{% equation %}\left(\kappa+\lambda\right)+\theta=\lambda+\left(\kappa+\theta\right){% endequation %} וגם {% equation %}\left(\kappa\cdot\lambda\right)\cdot\theta=\lambda\cdot\left(\kappa\cdot\theta\right){% endequation %} (אסוציאצטיביות)</li>


<li>{% equation %}\kappa\left(\lambda+\theta\right)=\kappa\lambda+\kappa\theta{% endequation %} (דיסטריביוטיביות)</li>


<li>{% equation %}\left(\kappa\lambda\right)^{\theta}=\kappa^{\theta}\lambda^{\theta}{% endequation %}</li>


<li>{% equation %}\kappa^{\lambda+\theta}=\kappa^{\lambda}\cdot\kappa^{\theta}{% endequation %}</li>


<li>{% equation %}\left(\kappa^{\lambda}\right)^{\theta}=\kappa^{\lambda\theta}{% endequation %}</li>


<li>אם {% equation %}\kappa\le\lambda{% endequation %} אז {% equation %}\kappa^{\theta}\le\lambda^{\theta}{% endequation %}</li>


<li>אם {% equation %}0<\lambda\le\theta{% endequation %} אז {% equation %}\kappa^{\lambda}\le\kappa^{\theta}{% endequation %}</li>


<li>{% equation %}\kappa^{0}=1{% endequation %}, {% equation %}1^{\kappa}=1{% endequation %} ו-{% equation %}0^{\kappa}=0{% endequation %} אם {% equation %}\kappa>0{% endequation %}</li>

</ul>

כל הטענות הללו הן טענות סטנדרטיות באריתמטיקה <strong>רגילה</strong> של מספרים, והן עוברות כמות שהן גם לאריתמטיקה של עוצמות, אבל כמובן שצריך להוכיח כל דבר פה. ההוכחות הן מה שאוהבים לכנות "תרגיל טוב": מצד אחד הן לא קשות, מצד שני לכו תוכיחו את הכל בעצמכם, עדיף לתת לסטודנטים לשבור את הראש על כמה מהן ואז שיעזבו את היתר בשקט.

יש דברים שהם קצת יותר ברורים מהאחרים: למשל, קומוטטיביות ואסוציאטיביות של חיבור וכפל נובעת מהקומוטטיביות והאסוציאטיביות של איחוד ומכפלה קרטזית של קבוצות (מכפלה קרטזית של שתי קבוצות היא לא בדיוק אסוציאטיבית אבל קרוב מספיק: {% equation %}\left(A\times B\right)\times C\sim A\times\left(B\times C\right){% endequation %} בצורה פשוטה). מעניין לחשוב על מה "נשבר" בקומוטטיביות בהקשר של חיבור וכפל של סודרים, הרי משתמשים גם שם באיחוד זר ובמכפלה קרטזית - אלא שבמקרה של סודרים יש מבנה נוסף של <strong>יחס סדר</strong> שמוגדר על הקבוצות הללו, והוא מוגדר בצורה מאוד לא סימטרית.

בכל זאת, בלי להוכיח <strong>משהו</strong> מהטענות אי אפשר, אז אני אבחר את החביבה עלי (ולטעמי הכי מורכבת להוכחה כאן): {% equation %}\left(\kappa^{\lambda}\right)^{\theta}=\kappa^{\lambda\theta}{% endequation %}. כלומר, אני צריך להראות שעבור שלוש קבוצות {% equation %}A,B,C{% endequation %} מתקיים {% equation %}\left(\left|A\right|^{\left|B\right|}\right)^{\left|C\right|}=\left|A\right|^{\left|B\right|\left|C\right|}{% endequation %}, כלומר שמתקיים {% equation %}\left|\left(A^{B}\right)^{C}\right|=\left|A^{B\times C}\right|{% endequation %}, כלומר שמתקיים {% equation %}\left(A^{B}\right)^{C}\sim A^{B\times C}{% endequation %}. כלומר, מספיק אם אראה פונקציה חח"ע ועל {% equation %}\Psi:A^{B\times C}\to\left(A^{B}\right)^{C}{% endequation %}: אני בונה התאמה {% equation %}\Psi{% endequation %} שמקבלת <strong>פונקציה</strong> בשני משתנים {% equation %}f:B\times C\to A{% endequation %}, ובונה מתוכה <strong>פונקציה שמחזירה פונקציות</strong>. אותי זה קצת הפחיד בהתחלה, אבל אפשר לחשוב על זה בדרך נוחה: על {% equation %}f\left(b,c\right){% endequation %} אני חושב בתור פונקציה במשתנה יחיד <strong>שתלויה בפרמטר</strong>. {% equation %}b{% endequation %} הוא המשתנה, ו-{% equation %}c{% endequation %} הוא הפרמטר. למשל, פונקציית הלוגריתם היא כזו: {% equation %}\log x{% endequation %} מניחה באופן מובלע שיש בסיס ללוגריתם. כשכותבים {% equation %}\log{% endequation %} בדרך כלל מתכוונים במובלע לבסיס 10, וכשכותבים {% equation %}\ln{% endequation %} מתכוונים לבסיס {% equation %}e{% endequation %} וכשכותבים {% equation %}\lg{% endequation %} מתכוונים לבסיס 2; באופן כללי כותבים {% equation %}\log_{b}x{% endequation %} כדי לציין שזה לוגריתם בבסיס {% equation %}b{% endequation %}. אז, קונספטואלית, {% equation %}\log_{b}x{% endequation %} היא פונקציה במשתנה יחיד ({% equation %}x{% endequation %}) שתלויה בפרמטר ({% equation %}b{% endequation %}). אם ממש רוצים, אפשר גם לחשוב עליה בתור פונקציה בשני משתנים, {% equation %}\left(x,b\right){% endequation %}. ההתאמה {% equation %}\Phi{% endequation %} עושה את הסוויץ' בין שתי נקודות המבט הללו.

הרעיון הוא כזה: נניח שיש לי ביד פונקציה של שני משתנים, {% equation %}f\left(x,y\right){% endequation %}, ואני מקבל ערך קונקרטי, {% equation %}c\in C{% endequation %}, שאני יכול להציב בתוך המשתנה השני. אז אני מציב אותו ומשאיר את המשתנה הראשון "פתוח" ומקבל פונקציה במשתנה אחד, {% equation %}f_{c}\left(x\right)=f\left(x,c\right){% endequation %}. הטריק הזה שבו אני מקבל פונקציה של כמה משתנים, מבצע בה "הצבה חלקית" ומקבל פונקציה חדשה נקרא Currying, על שם הלוגיקאי והפילוסוף הסקל קרי. אם חושבים על מה שהלך בטריק הזה, מה שקרה הוא שלכל ערך {% equation %}c\in C{% endequation %} אני ייצרתי פונקציה {% equation %}f_{c}:B\to A{% endequation %}. כלומר, יש לי פונקציה {% equation %}\Phi_{f}:C\to A^{B}{% endequation %} שמוגדרת על ידי {% equation %}\Phi_{f}\left(c\right)=f_{c}{% endequation %}.

עכשיו אפשר לחזור אל האובייקט שאני אמור להראות את קיומו: פונקציה חח"ע ועל {% equation %}\Psi:A^{B\times C}\to\left(A^{B}\right)^{C}{% endequation %}. אני יכול סוף סוף להגדיר אותו, וזה יוצא די פשוט עם הסימונים שנתתי:

{% equation %}\Psi\left(f\right)=\Phi_{f}{% endequation %}

למה זו פונקציה חח"ע ועל? ראשית, אם {% equation %}\Psi\left(f\right)=\Psi\left(g\right){% endequation %}, כלומר אם {% equation %}\Phi_{f}=\Phi_{g}{% endequation %}, זה אומר שלכל {% equation %}c\in C{% endequation %} {% equation %}\Phi_{f}\left(c\right)=\Phi_{g}\left(c\right){% endequation %}, כלומר לכל {% equation %}c\in C{% endequation %} {% equation %}f_{c}=g_{c}{% endequation %}, כלומר לכל {% equation %}\left(b,c\right){% endequation %} מתקיים {% equation %}f\left(b,c\right)=f_{c}\left(b\right)=g_{c}\left(b\right)=g\left(b,c\right){% endequation %}, ומכאן ש-{% equation %}f=g{% endequation %}, מה שמראה ש-{% equation %}\Psi{% endequation %} חח"ע.

שנית, אם יש לנו {% equation %}\Phi\in\left(A^{B}\right)^{C}{% endequation %} <strong>כלשהי</strong>, אני אגדיר פונקציה {% equation %}f\in A^{B\times C}{% endequation %} באופן הבא:

{% equation %}f\left(b,c\right)\triangleq\Phi\left(c\right)\left(b\right){% endequation %}

כלומר, אני קודם כל מחשב את {% equation %}\Phi\left(c\right){% endequation %}, מקבל פונקציה ב-{% equation %}A^{B}{% endequation %}, ואז מפעיל את הפונקציה הזו על {% equation %}b{% endequation %} ומחזיר את התוצאה. כעת, אני כזכור מסמן {% equation %}\Psi\left(f\right)=\Phi_{f}{% endequation %}; אם אני אראה ש-{% equation %}\Phi=\Phi_{f}{% endequation %}, סיימנו. בשביל להראות את זה, צריך להראות שהן מזדהות על כל הקלטים, כלומר לכל {% equation %}c\in C{% endequation %} מתקיים {% equation %}\Phi\left(c\right)=\Phi_{f}\left(c\right){% endequation %}. הפלטים הללו הם בעצמם פונקציות על {% equation %}B{% endequation %}, אז צריך להראות שלכל {% equation %}b\in B{% endequation %} מתקיים {% equation %}\Phi\left(c\right)\left(b\right)=\Phi_{f}\left(c\right)\left(b\right){% endequation %}, אבל זה נובע ישירות מההגדרה:

{% equation %}\Phi_{f}\left(c\right)\left(b\right)=f_{c}\left(b\right)=f\left(b,c\right)=\Phi\left(c\right)\left(b\right){% endequation %}

וזה מסיים את ההוכחה. לא כל כך נורא! זה <strong>באמת</strong> תרגיל טוב לנסות להוכיח חלק מפעולות החשבון האחרות.

<h2>ועכשיו... בואו נדבר על השערת הרצף</h2>

לפני שנדבר על השערת הרצף, בואו נשים לב למשהו קל שנובע ממה שכבר ראינו: אם אני מסמן ב-{% equation %}\mathcal{P}\left(A\right){% endequation %} את קבוצת החזקה של {% equation %}A{% endequation %}, כלומר קבוצת כל תתי-הקבוצות של {% equation %}A{% endequation %} (היא קיימת כי יש אקסיומה מיוחדת שמניחה שהיא קיימת), אז {% equation %}\left|\mathcal{P}\left(A\right)\right|=2^{\left|A\right|}{% endequation %}.

ההוכחה די פשוטה: צריך להראות ש-{% equation %}\mathcal{P}\left(A\right)\sim2^{A}{% endequation %}. בהינתן {% equation %}B\in\mathcal{P}\left(A\right){% endequation %} נעביר אותה אל הפונקציה {% equation %}\chi_{B}:A\to2{% endequation %} (בואו נזכר ש-{% equation %}2=\left\{ 0,1\right\} {% endequation %} על פי ההגדרות שלנו) שמוגדרת על ידי

{% equation %}\chi_{B}\left(a\right)=\begin{cases} 1 & a\in B\\ 0 & a\notin B \end{cases}{% endequation %}

זה מה שנקרא <strong>הפונקציה המציינת</strong> של {% equation %}B{% endequation %} וקל לראות שזו התאמה חח"ע ועל. זה משתלב יפה עם הבחירה שלנו לסמן את {% equation %}\mathcal{P}\left(A\right){% endequation %} לפעמים בתור {% equation %}2^{A}{% endequation %}; אלו לא קבוצות זהות מבחינה פורמלית, אבל הן בתכל'ס אותו הדבר עד כדי סימונים.

עכשיו, משפט קנטור על קבוצת החזקה מלמד אותנו ש-{% equation %}\left|A\right|<2^{\left|A\right|}{% endequation %}. בפרט עבור {% equation %}A=\mathbb{N}{% endequation %}. עבורה, כזכור, סימנו {% equation %}\left|\mathbb{N}\right|=\aleph_{0}{% endequation %} כך שאנחנו יודעים ש-{% equation %}\aleph_{0}<2^{\aleph_{0}}{% endequation %}, ומכאן ש-{% equation %}\aleph_{1}\le2^{\aleph_{0}}{% endequation %}. האם מתקיים שוויון? האם {% equation %}\aleph_{1}=2^{\aleph_{0}}{% endequation %}? ההשערה שמתקיים שוויון כזה נקראת <strong>השערת הרצף</strong>.

השערת הרצף הועלתה במקור בידי גאורג קנטור, ממציא תורת הקבוצות. בנאום 23 הבעיות המתמטיות המפורסם שלו מ-1900, דויד הילברט הציב את השערת הרצף בתור השאלה הפתוחה הראשונה ברשימה. קנטור עצמו האמין שהתשובה חיובית וש-{% equation %}\aleph_{1}=2^{\aleph_{0}}{% endequation %}; שקבוצה מ"עוצמת ביניים" כזו בין {% equation %}\aleph_{0}{% endequation %} ובין {% equation %}2^{\aleph_{0}}{% endequation %} תהיה דבר מוזר ביותר, אבל הוכחה - לא נמצאה. בינתיים עבר קצת זמן, ועל תורת הקבוצות עברו תהפוכות עם גילוי הפרדוקס של ראסל. 

כשהאבק הזה שכך, תורת הקבוצות התהדרה במערכת אקסיומות מפוארת - ZFC (צרמלו-פרנקל עם אקסיומת הבחירה). המערכת המפוארת הזו משרתת היטב את המתמטיקה עד היום, ולא נתגלו בה בעיות מהותיות - והמערכת הזו <strong>חסרת יכולת</strong> להכריע האם השערת הרצף נכונה או לא. יש לנו הוכחה מתמטית שלא ניתן להוכיח או להפריך את השערת הרצף בעזרת ZFC; הוכחה שחצי ממנה התגלה במקור בידי קורט גדל בשנות השלושים, והחצי השני התגלה בידי פול כהן בשנות השישים. לצורך ההוכחה, כהן פיתח טכניקה חדשה שנקראת <strong>כפייה</strong> (Forcing) שאפשר להשתמש בה כדי לתת את ההוכחה המלאה, בלי להזדקק להוכחה המקורית של גדל.

המטרה המרכזית שלי בסדרת הפוסטים הזו על תורת הקבוצות היא להציג את טכניקת הכפייה וההוכחה שהשערת הרצף בלתי תלויה ב-ZFC. האם אצליח להשיג את המטרה הזו? אני עוד לא בטוח. ההיכרות שלי עם ההוכחה הזו היא שטחית למדי (למרות שקראתי את כולה, אני לא ממש בקיא בכל ה"מסביב" ובשימושים נוספים של הטכניקה) וזו בהחלט הוכחה שמצריכה הסבר של התמונה הגדולה ברוב שלביה או שקל ללכת לאיבוד. נקווה לטוב.

לעת עתה, בואו נדבר על {% equation %}\mathbb{R}{% endequation %}. הבטחתי כבר כמה פעמים שאגיד מהו {% equation %}\left|\mathbb{R}\right|{% endequation %}, ואין פה סוד גדול: {% equation %}\left|\mathbb{R}\right|=2^{\aleph_{0}}{% endequation %}, כך שהשערת הרצף היא השאלה האם קיימת קבוצה של ממשיים שהיא מעוצמה שונה הן מהטבעיים והן מהממשיים. אבל איך אפשר להוכיח ש-{% equation %}\left|\mathbb{R}\right|=2^{\aleph_{0}}{% endequation %}? אני אציג פה הוכחה חביבה למדי שמסתמכת על משפט <a href="https://gadial.net/2016/11/30/csb_theorem_hilbert_hotel_style/">קנטור-שרדר-ברנשטיין</a>: אני אוכיח ש-{% equation %}\left|\mathbb{R}\right|\le2^{\aleph_{0}}{% endequation %} וגם {% equation %}\left|\mathbb{R}\right|\ge2^{\aleph_{0}}{% endequation %} ומזה ינבע {% equation %}\left|\mathbb{R}\right|=2^{\aleph_{0}}{% endequation %}.

כיוון אחד הוא קל: הגדרה סטנדרטית של {% equation %}\mathbb{R}{% endequation %} היא באמצעות <strong>חתכי דדקינד</strong>. בצורה זו, כל {% equation %}r\in\mathbb{R}{% endequation %} מיוצג על ידי קבוצה {% equation %}\left\{ q\in\mathbb{Q}\ |\ q<r\right\} {% endequation %}. ספציפית, מתקיים {% equation %}r=\sup\left\{ q\in\mathbb{Q}\ |\ q<r\right\} {% endequation %}. מכאן שיש לנו התאמה חח"ע מ-{% equation %}\mathbb{R}{% endequation %} אל {% equation %}2^{\mathbb{Q}}{% endequation %}, כלומר {% equation %}\left|\mathbb{R}\right|\le\left|2^{\mathbb{Q}}\right|=2^{\aleph_{0}}{% endequation %}.

הכיוון השני מעניין יותר. כדי להראות {% equation %}2^{\aleph_{0}}\le\left|\mathbb{R}\right|{% endequation %} די להראות התאמה חח"ע מאוסף הסדרות הבינאריות אל {% equation %}\mathbb{R}{% endequation %}, כש"סדרה בינארית" היא פונקציה מ-{% equation %}\mathbb{N}{% endequation %} אל {% equation %}\left\{ 0,1\right\} {% endequation %} שאפשר פשוט לכתוב בתור {% equation %}b_{0},b_{1},b_{2},\ldots{% endequation %} עם {% equation %}b_{i}\in\left\{ 0,1\right\} {% endequation %}. כמובן, זה לא משנה בפועל אם בסדרה מופיע 1 או אם נחליף את כל המופעים של 1 ב-2, אז בואו נניח שהסדרה {% equation %}\left\{ b_{i}\right\} _{i=1}^{\infty}{% endequation %} שלנו מקיימת דווקא {% equation %}b_{i}\in\left\{ 0,2\right\} {% endequation %} כי זה מאוד יקל עלינו עוד שניה.

עכשיו נכניס לתמונה את <a href="https://gadial.net/2010/04/21/cantor_set/">קבוצת קנטור</a>. יש לי כבר פוסט עליה, אז הנה תזכורת קצרה: הרעיון בקבוצת קנטור הוא לקחת את הקטע {% equation %}\left[0,1\right]{% endequation %}, לחלק אותו לשלושה קטעים שווים, ולמחוק את הקטע האמצעי, <strong>לא כולל</strong> נקודות הקצה שלו. זה מניב לנו את איחוד הקטעים {% equation %}\left[0,\frac{1}{3}\right]\cup\left[\frac{2}{3},1\right]{% endequation %}. עכשיו לוקחים את שני הקטעים הללו ועושים את אותו דבר עליהם - מעיפים את השליש האמצעי, משאירים את היתר. וככה זה נמשך עוד ועוד ועוד עד אינסוף, והתוצאה היא קבוצה שה<strong>מידה</strong> שלה היא 0. 

בלי להיכנס להגדרה של מידה, הרעיון הוא שאם אפשר לכסות קבוצה על ידי אוסף של קטעים קטנים כרצוננו (שסכום האורכים שלהם קטן מאיזה {% equation %}\varepsilon>0{% endequation %} נתון) אז היא ממידה אפס, וזה מה שקורה עם קבוצת קנטור - בכל שלב בבניה היא מכוסה על ידי אוסף הקטעים שבידינו באותו שלב, והאורך הכולל של הקטעים בשלב {% equation %}n{% endequation %} הוא {% equation %}2^{n}\cdot\left(\frac{1}{3}\right)^{n}=\left(\frac{2}{3}\right)^{n}{% endequation %} - שואף לאפס כש-{% equation %}n{% endequation %} שואף לאינסוף.

והנה זה פלא, למרות שהסרנו מהקבוצה את כל ה"אורך" שלה, עדיין היא לא בת מניה; אפשר להוכיח שאיבר שייך לקבוצת קנטור אם ורק אם אפשר לכתוב אותו בתור {% equation %}\sum_{n=0}^{\infty}\frac{a_{i}}{3^{n}}{% endequation %} כך ש-{% equation %}a_{i}\in\left\{ 0,2\right\} {% endequation %}. הרעיון הוא לפתח את האיבר לייצוג <strong>טרנרי</strong> (בבסיס 3) ולהראות שאיבר מוסר מהבניה, כלומר הוא שייך לקטע אמצעי כלשהו בשלב הבניה ה-{% equation %}n{% endequation %}, רק אם הספרה במקום ה-{% equation %}n{% endequation %} בכל ייצוג טרנרי שלו היא 1 (האינטואיציה הלא מדויקת עד הסוף היא הספרה 0 מכניסה אותו לחלק השמאלי והספרה 2 מכניסה אותו לחלק הימני של הקטע שחולק לשלושה חלקים; הזסיבה שצריך להיזהר היא שיש מספרים עם שני ייצוגים טרנריים שונים ומספיק ש-1 לא יופיע בכלל באחד מהם). 

כל הסיפור הזה נותן לנו את ההתאמה החח"ע שמראה ש-{% equation %}2^{\aleph_{0}}\le\left|\mathbb{R}\right|{% endequation %}, ולכן מסיים את ההוכחה ש-{% equation %}\left|\mathbb{R}\right|=2^{\aleph_{0}}{% endequation %}, מה שנותן לנו אפשרות לנסח את השערת הרצף גם בניסוח המקובל שלה, עם הממשיים.

עוד דרך אחת לנסח את השערת הרצף היא באמצעות ההגדרה של מה שנקרא מספרי {% equation %}\beth{% endequation %}, שמקבילים למספרי {% equation %}\aleph{% endequation %} שכבר ראינו. הם מוגדרים בצורה שאולי הייתה נראית לנו מתבקשת במבט ראשון כדי לתפוס את כל העוצמות:

<ul> <li>{% equation %}\beth_{0}=\omega{% endequation %}</li>


<li>{% equation %}\beth_{\alpha+1}=2^{\beth_{\alpha}}{% endequation %} לכל סודר {% equation %}\alpha{% endequation %}.</li>


<li>{% equation %}\beth_{\alpha}=\text{sup}\left\{ \beth_{\beta}\ |\ \beta<\alpha\right\} {% endequation %} כאשר {% equation %}\alpha{% endequation %} הוא סודר גבולי.</li>

</ul>

בניסוח הזה, השערת הרצף היא הטענה {% equation %}\aleph_{1}=\beth_{1}{% endequation %}, ואפשר לנסח טענה חזקה יותר - <strong>השערת הרצף המוכללת</strong>, שאומרת ש-{% equation %}\aleph_{\alpha}=\beth_{\alpha}{% endequation %} לכל סודר {% equation %}\alpha{% endequation %}. אני לא אתעסק עם ההשערה הזו בפוסטים שלי כרגע - השערת הרצף הרגילה זה די והותר עבורי... 