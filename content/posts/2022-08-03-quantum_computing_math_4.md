---
title: "חישוב קוונטי בגישה מתמטית, חלק ד': שערים קוונטיים"
layout: post
categories:
  - חישוב קוונטי
tags:
  - חישוב קוונטי
description: 'איך מייצרים מצבים שזורים? איך מודדים מצבים של שני קיוביטים ויותר? בפוסט הזה אנחנו מסיימים להציג את המתמטיקה הבסיסית שנדרשת כדי לתאר חישוב קוונטי'
image: "2022/bell_pair_circuit.png"
---


<h2>מעגלים קוונטיים</h2>

<a href="https://gadial.net/2022/08/01/quantum_computing_math_3/">בפוסט הקודם שלי</a> על חישוב קוונטי ראינו איך בהינתן מערכת של {% equation %}n{% endequation %} קיוביטים אנחנו יכולים "לתרגם" אופרטור שפועל על קיוביט אחד לאופרטור שפועל על כל המערכת: אם האופרטור הוא למשל {% equation %}X{% endequation %} שמופעל על הקיוביט הראשון, אנחנו בונים את האופרטור {% equation %}X\otimes I\otimes I\otimes\cdots\otimes I{% endequation %} שפירושו "תפעיל את {% equation %}X{% endequation %} על הקיוביט הראשון ועל היתר אל תעשה כלום". אפשר כמובן גם לעשות דברים כמו {% equation %}X\otimes Z{% endequation %} שפירושים "תפעיל את {% equation %}X{% endequation %} על הקיוביט הראשון ואת {% equation %}Z{% endequation %} על הקיוביט השני", ודבר כזה יכול להתרחש במחשב קוונטי אמיתי על ידי כך שקודם מפעילים את {% equation %}X{% endequation %} על הקיוביט הראשון (כלומר עושים {% equation %}X\otimes I{% endequation %}) ואז את {% equation %}Z{% endequation %} על הקיוביט השני (כלומר עושים {% equation %}I\otimes Z{% endequation %}).

הסיטואציה מזכירה מאוד חישוב רגיל באמצעות <strong>מעגלים לוגיים</strong>, שבהם יש לנו כמה ביטים, ואנחנו מפעילים כל פעם פעולות כלשהן עליהם - פעולת NOT, פעולת AND וכדומה. לפעולות הללו יש שם - <strong>שערים לוגיים</strong>. לכן, בהתאם, לפעולות על קיוביטים קוראים <strong>שערים קוונטיים</strong>. בפרט כשמדברים על שער קוונטי מתכוונים לפעולה על מספר קטן של קיוביטים - אחד או שניים, בדרך כלל, אבל אין לזה הגדרה פורמלית של ממש.

עד כה כל מה שראינו היו שערים של קיוביט אחד. לא נזקקנו ליותר מזה - כאמור, גם {% equation %}X\otimes Z{% endequation %} זה בעצם הפעלה של שני שערים של קיוביט בודד, בזה אחר זה. אבל ברור לחלוטין שאנחנו <strong>חייבים</strong> גם שער של שני קיוביטים. למה? כי בלי זה אין לנו איך לייצר מצב שזור, כמו {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %} שראינו קודם. אופרטור כמו {% equation %}X\otimes Z{% endequation %} פועל על כל קיוביט בנפרד, ולכן אם לפני ההפעלה שלו היו לנו שני קיוביטים מבודדים שלא קשורים זה לזה, אחרי ההפעלה שלו כל אחד מהקיוביטים הללו יתפתח באופן עצמאי ועדיין לא יווצר ביניהם קשר. כשם שהמצב השזור שאנחנו רוצים להגיע אליו לא ניתן לביטוי בתור {% equation %}u\otimes w{% endequation %}, כך גם האופרטור שאני צריך יהיה כזה שלא ניתן לביטוי בתור {% equation %}A\otimes B{% endequation %}.

מי שאשתמש בו הוא אופרטור על שני קיוביטים שנקרא CNOT, או CX. את ה-C צריך לקרוא בתור Controlled; הרעיון הוא שזה שער שעל קיוביט מסוים פועל או כמו הזהות (לא עושה כלום) או כמו {% equation %}X{% endequation %} (והרי ראינו ש-{% equation %}X{% endequation %} זה כמו פעולת NOT), כשהשאלה האם הוא יעשה משהו או לא תלויה בקיוביט אחר - קיוביט הבקרה.

הדרך להגדיר פורמלית אופרטור היא על ידי פעולתו על אברי בסיס - כאן אני עוסק באופרטור שפועל על שני קיוביטים, אז אני אגדיר אותו על ארבעת אברי הבסיס הסטנדרטי המתאימים:

{% equation %}\text{CX}\left|00\right\rangle =\left|00\right\rangle {% endequation %}

{% equation %}\text{CX}\left|01\right\rangle =\left|01\right\rangle {% endequation %}

{% equation %}\text{CX}\left|10\right\rangle =\left|11\right\rangle {% endequation %}

{% equation %}\text{CX}\left|11\right\rangle =\left|10\right\rangle {% endequation %}

כאן הבקרה היא הקיוביט הראשון (השמאלי). אם היא 0, כמו בשתי השורות הראשונות, {% equation %}\text{CX}{% endequation %} לא משנה כלום; אם היא 1, {% equation %}\text{CX}{% endequation %} הופך את הקיוביט השני. בכתיב מטריציוני זה נראה כך:

{% equation %}\text{CX}=\left(\begin{array}{cccc} 1 & 0 & 0 & 0\\ 0 & 1 & 0 & 0\\ 0 & 0 & 0 & 1\\ 0 & 0 & 1 & 0 \end{array}\right){% endequation %}

כלומר, אפשר לחשוב על האופרטור הזה בתור מטריצת בלוקים:

{% equation %}\text{CX}=\left(\begin{array}{cc} I & 0\\ 0 & X \end{array}\right){% endequation %}

אין משהו קסום ב-{% equation %}\text{X}{% endequation %} כאן, אפשר להגדיר אופרטור "נשלט" שכזה עבור כל אופרטור של קיוביט בודד, למשל אפשר להגדיר

{% equation %}\text{CZ}=\left(\begin{array}{cc} I & 0\\ 0 & Z \end{array}\right){% endequation %}

אבל בדרך כלל נזדקק רק ל-{% equation %}\text{CX}{% endequation %}.

שימו לב שבבירור {% equation %}\text{CX}{% endequation %} לא יכול להיכתב בתור {% equation %}A\otimes B{% endequation %}. בשביל שזה יקרה, {% equation %}B{% endequation %} צריכה להיות מטריצה שכפל בסקלר אחר יהפוך אותה ל-{% equation %}I{% endequation %} וכפל בסקלר אחר יהפוך אותה ל-{% equation %}X{% endequation %}; אין דבר כזה.

איך {% equation %}\text{CX}{% endequation %} עוזר לנו לייצר מצב שזור? קלי קלות. בואו נבצע חישוב קוונטי שכולל שני שלבים, על קלט שמאותחל ל-{% equation %}\left|00\right\rangle {% endequation %}:

<ol> <li>מפעילים שער {% equation %}H{% endequation %} על הקיוביט הראשון.</li>


<li>מפעילים שער {% equation %}\text{CX}{% endequation %} על הקיוביט השני כשהוא נשלט על ידי הקיוביט הראשון.</li>

</ol>

את החישוב הזה מתארים באמצעות מעגל קוונטי שנראה כך:

<img src="{{site.baseurl}}{{site.post_images}}/2022/bell_pair_circuit.png" alt=""/>

הרעיון בתיאור מעגל כזה הוא שהקיוביטים מסודרים בשורות. השורה הראשונה מתאימה לקיוביט הראשון והשניה לשני. ה-{% equation %}\left|0\right\rangle {% endequation %} שמופיעים בצד שמאל הם הערכים שאליהם מאתחלים את הקיוביטים במעגל. אחר כך כיוון הקריאה הוא משמאל לימין. בהתחלה הקיוביט הראשון נכנס לשער {% equation %}H{% endequation %}, בזמן שהשני פשוט "זורם" בלי שיופעל עליו אף שער. אחר כך מגיע שער ה-{% equation %}\text{CX}{% endequation %} שמתואר באמצעות נקודה שחורה על קיוביט הבקרה, וסימן {% equation %}\oplus{% endequation %} על הקיוביט שיתהפך (כי אפשר לחשוב על הפעולה ששער CX מבצע כמו על פעולת XOR, {% equation %}\oplus{% endequation %}, בין שני ביטים רגילים, כשהפלט נכנס לביט השני).

בואו נבצע את החישוב הפורמלי שהמעגל מבצע:

{% equation %}H_{1}\left(\left|00\right\rangle \right)=H\left(\left|0\right\rangle \right)\left|0\right\rangle =\left(\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}\right)\left|0\right\rangle =\frac{\left|00\right\rangle +\left|10\right\rangle }{\sqrt{2}}{% endequation %}

אני מקווה שבשלב הזה כבר ברור בדיוק מה הולך בחישוב (ולהבא אני כנראה אדלג על שלבי הביניים). מי שעדיין מוטרד יכול כמובן לחשב את המטריצה של {% equation %}H_{1}=H\otimes I{% endequation %}, להפעיל אותה ולראות מה קורה.

הפעלת ה-{% equation %}\text{CX}{% endequation %} תתבצע על פי התיאור על אברי הבסיס שנתתי למעלה:

{% equation %}\text{CX}\left(\frac{\left|00\right\rangle +\left|10\right\rangle }{\sqrt{2}}\right)=\frac{\text{CX}\left|00\right\rangle +\text{CX}\left|10\right\rangle }{\sqrt{2}}=\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %}

והנה, באופן בלתי מפתיע ביותר, קיבלנו את {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %} שהבטחתי, ועל הדרך למדנו איך מתאים שערים קוונטיים וראינו אותם בפעולה.

עכשיו, כשאולי לרגע אחד אנחנו מרגישים שהכל טוב ואפשר לנשום, בואו נסבך את הכל הרבה יותר - נתחיל לדבר על איך עובדות <strong>מדידות</strong> כשיש לנו יותר מקיוביט אחד.

<h2>מדידות, באופן כללי</h2>

בואו נזכיר איך עובדת מדידה של קיוביט יחיד: יש לנו מצב {% equation %}\alpha\left|0\right\rangle +\beta\left|1\right\rangle {% endequation %}. כשאנחנו מודדים אותו, אנחנו מגרילים בהסתברות {% equation %}\left|\alpha\right|^{2}{% endequation %} את התוצאה 0, ומעבירים את המצב למצב {% equation %}\left|0\right\rangle {% endequation %}; ובהסתברות {% equation %}\left|\beta\right|^{2}{% endequation %} את התוצאה 1 ומעבירים את המצב למצב {% equation %}\left|1\right\rangle {% endequation %}. זה היה המושג הפשטני שהצגתי עד כה - פשטני <strong>טיפה</strong> יותר מדי, כפי שנראה בהמשך.

עכשיו, אם יש לנו מצב קוונטי כללי של שני קיוביטים, {% equation %}\alpha\left|00\right\rangle +\beta\left|01\right\rangle +\gamma\left|10\right\rangle +\delta\left|11\right\rangle {% endequation %}, אפשר לעשות תעלול דומה. האילוץ שהמצב הוא מנורמה 1 גורר ש-{% equation %}\left|\alpha\right|^{2}+\left|\beta\right|^{2}+\left|\gamma\right|^{2}+\left|\delta\right|^{2}=1{% endequation %}, כך שאפשר לחשוב על כל המספרים הללו כמגדירים הסתברות, ואז מה שיקרה במדידה הוא שנבחר את {% equation %}\left|00\right\rangle {% endequation %} בהסתברות {% equation %}\left|\alpha\right|^{2}{% endequation %}, נחזיר 00 ונעבור למצב {% equation %}\left|00\right\rangle {% endequation %}, וכן הלאה. זו מדידה "של שני הקיוביטים בבת אחת".

אבל אני רוצה לעשות משהו שונה. אני כבר יודע למדוד קיוביט בודד; מה יקרה אם יש לי מערכת של שני קיוביטים, במצב שזור אפילו, אבל אני מודד רק אחד מהקיוביטים? איך המערכת תשתנה כתוצאה מכך? התיאור המתמטי שהשתמשתי בו עד כה לא מכסה את זה.

אני <strong>יכול</strong> לנפנף בידיים. נניח שאני רוצה למדוד את {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %} לפי הקיוביט הראשון. אז אני יכול לומר את הדבר הבא: המצב הזה סימטרי בין {% equation %}\left|00\right\rangle {% endequation %} ובין {% equation %}\left|11\right\rangle {% endequation %} ולכן ההסתברות שהמדידה של הקיוביט הראשון תיתן {% equation %}0{% endequation %} היא {% equation %}\frac{1}{2}{% endequation %} וההסתברות שהיא תיתן {% equation %}1{% endequation %} היא {% equation %}\frac{1}{2}{% endequation %}. במקרה הראשון, המערכת תעבור למצב {% equation %}\left|00\right\rangle {% endequation %} שהוא היחיד שבו הקיוביט הראשון הוא 0, ובמקרה השני היא תעבור למצב {% equation %}\left|11\right\rangle {% endequation %}. נפנוף הידיים הזה נכון אבל ממש קשה להבין ממנו מה בעצם אמור לקרות באופן כללי. זה כן מלמד אותנו כבר עכשיו על התופעה המגניבה שיש למצב {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %}: המדידה של הקיוביט <strong>הראשון</strong> משפיעה גם על הקיוביט <strong>השני</strong>. אם טרם מדדנו את הקיוביט הראשון, מדידה של הקיוביט השני יכולה להניב 0 או 1 בהסתברות חצי-חצי. אבל אם כבר מדדנו את הקיוביט הראשון, אז מדידה של הקיוביט השני תניב <strong>בודאות מוחלטת</strong> את אותה תוצאה כמו זו שהתקבלה במדידת הקיוביט הראשון. והמופלא ביותר הוא שזה קורה גם אם הקיוביט הללו מיוצגים על ידי יישויות פיזיקליות שבכלל לא סמוכות אחת לשניה; זה מה שפרדוקס EPR, <a href="https://gadial.net/2014/08/03/heisenberg_epr_and_bell/">שכתבתי עליו פעם פוסט</a>, עוסק בו.

הנה עוד דרך לנפנף בידיים שאולי תיתן קצת יותר אינטואיציה: אפשר לכתוב

{% equation %}\alpha\left|00\right\rangle +\beta\left|01\right\rangle +\gamma\left|10\right\rangle +\delta\left|11\right\rangle =\left|0\right\rangle \left(\alpha\left|0\right\rangle +\beta\left|1\right\rangle \right)+\left|1\right\rangle \left(\gamma\left|0\right\rangle +\delta\left|1\right\rangle \right){% endequation %}

ואז ה"מקדם" של {% equation %}\left|0\right\rangle {% endequation %} הוא {% equation %}\left(\alpha\left|0\right\rangle +\beta\left|1\right\rangle \right){% endequation %}. זה לא מספר אלא וקטור, אבל אפשר לקחת לו נורמה ולקבל {% equation %}\left|\alpha\right|^{2}+\left|\beta\right|^{2}{% endequation %}, וזו ההסתברות לקבל 0 בקיוביט הראשון. אם זו תהיה התוצאה, אז המערכת תעבור למצב {% equation %}\left|0\right\rangle \left(\alpha\left|0\right\rangle +\beta\left|1\right\rangle \right){% endequation %} הזה, רק שהוא לא מנורמל; כדי לנרמל אותו, נחלק ב-{% equation %}\sqrt{\left|\alpha\right|^{2}+\left|\beta\right|^{2}}{% endequation %} ונקבל שעברנו למצב {% equation %}\frac{\left|0\right\rangle \left(\alpha\left|0\right\rangle +\beta\left|1\right\rangle \right)}{\sqrt{\left|\alpha\right|^{2}+\left|\beta\right|^{2}}}{% endequation %}. אפשר, אפשר לנפנף ככה בידיים, זה באמת עובד. אבל זה מרגיש גם מסובך יחסית לנפנוף ידיים, וגם (לפחות עבורי) לא נותן תחושה שאנחנו על קרקע יציבה וממש מבינים מה אנחנו עושים.

כל זה נועד לרכך קצת את ההגדרה שאציג עכשיו - ההגדרה <strong>הכללית ביותר</strong> של מדידה שאזדקק לה, שהיא קצת כבדה מתמטית אבל פותרת אחת ולתמיד את כל חוסר הנוחות שענייני המדידה גורמים לנו. ראינו כבר שיש כל מני סוגים של מדידות - של שני הקיוביטים ביחד, של כל קיוביט בנפרד, על פי הבסיס {% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %}, על פי הבסיס {% equation %}\left|+\right\rangle ,\left|-\right\rangle {% endequation %}... ההגדרה שלנו תקיף את כל המקרים הללו. שימו לב שההגדרה של מדידה בכלל לא נכנסת לשאלה איך מבצעים מדידה <strong>בפועל</strong>; זה תלוי במערכת הפיזיקלית שאיתה מממשים את הקיוביטים, וזה בדרך כלל תהליך מסובך משמעותית ממה שאני מתאר פה. כל היופי בחישוב קוונטי מבחינתי הוא ביכולת שלי לבצע אבסטרקציה לפרטים הפיזיקליים המסובכים. אז למרות שהמושג שאציג יהיה מאוד כללי, זה לא אומר שמחשב קוונטי יוכל לבצע את כל המדידות הללו - אבל את המדידה ה"פשוטה" של קיוביט יחיד על פי הבסיס {% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %} הוא יוכל לבצע.

אם כן, נניח שיש לנו {% equation %}n{% endequation %} קיוביטים, כלומר המצב הקוונטי שלנו הוא איבר של {% equation %}\mathbb{C}^{2^{n}}{% endequation %}. אז <strong>מדידה</strong> עם {% equation %}k{% endequation %} תוצאות אפשריות מוגדרת על ידי סדרה של <strong>אופרטורי מדידה </strong>{% equation %}M_{0},M_{1},\ldots,M_{k-1}{% endequation %}, כך שכל {% equation %}M_{i}{% endequation %} כזה הוא אופרטור {% equation %}M_{i}:\mathbb{C}^{2^{n}}\to\mathbb{C}^{2^{n}}{% endequation %}, והדרישה היחידה שלנו מהאופרטורים היא שיתקיים

{% equation %}\sum_{i=0}^{k-1}M_{i}^{\dagger}M_{i}=I{% endequation %}

אין דרישות אחרות! האופרטורים <strong>לא</strong> חייבים להיות אוניטריים! המספר {% equation %}k{% endequation %} <strong>לא</strong> חייב להיות 2, או {% equation %}2^{n}{% endequation %} או שום דבר אחר! יש לנו חופש מלא כאן!

בהינתן מצב {% equation %}\left|\psi\right\rangle \in\mathbb{C}^{2^{n}}{% endequation %}, ההסתברות לקבל את התוצאה ה-{% equation %}i{% endequation %}-ית במדידה שלו היא

{% equation %}p\left(i\right)=\left\langle \psi\right|M_{i}^{\dagger}M_{i}\left|\psi\right\rangle {% endequation %} (לא להיבהל! תכף אזכיר מה זה {% equation %}\left\langle \psi\right|{% endequation %})

ואם התוצאה ה-{% equation %}i{% endequation %} עלתה בגורל, המצב הקוונטי {% equation %}\left|\psi\right\rangle {% endequation %} עובר למצב החדש

{% equation %}\frac{M\left|\psi\right\rangle }{\sqrt{\left\langle \psi\right|M^{\dagger}M\left|\psi\right\rangle }}{% endequation %}

זהו, זו כל ההגדרה. עכשיו צריך

<ol> <li>להסביר מה בשם שרדינגר הולך כאן.</li>


<li>להסביר למה זה תקין מבחינה מתמטית.</li>


<li>להסביר איך זה בעצם מכליל את כל המדידות שעליהן כבר דיברנו.</li>

</ol>

עדיף לי להתחיל מ-3: תמיד יותר קל להבין דברים כשיש לנו דוגמאות מול העיניים. נניח שאנחנו במרחב של קיוביט בודד, אז אופרטורי המדידה שלי יהיו {% equation %}M:\mathbb{C}^{2}\to\mathbb{C}^{2}{% endequation %}; כאלו דברים קל לייצג עם מטריצות {% equation %}2\times2{% endequation %}. המדידה "הרגילה" מוגדרת על ידי זוג המטריצות

{% equation %}M_{0}=\left(\begin{array}{cc} 1 & 0\\ 0 & 0 \end{array}\right){% endequation %}

{% equation %}M_{1}=\left(\begin{array}{cc} 0 & 0\\ 0 & 1 \end{array}\right){% endequation %}

המטריצות הללו מקיימות {% equation %}M_{i}^{\dagger}M_{i}=M_{i}{% endequation %} ולכן באופן מיידי מקבלים {% equation %}\sum_{i=0}^{k-1}M_{i}^{\dagger}M_{i}=I{% endequation %}, כלומר המטריצות הללו אכן מגדירות לי מדידה חוקית על פי ההגדרה שנתתי.

עכשיו, מה קורה כאשר מודדים את המצב {% equation %}\left|\psi\right\rangle =\alpha\left|0\right\rangle +\beta\left|1\right\rangle {% endequation %}? ההסתברות לקבל 0 היא {% equation %}p\left(0\right)=\left\langle \psi\right|M_{0}^{\dagger}M_{0}\left|\psi\right\rangle {% endequation %}. איך מחשבים את זה? ראשית, אני יכול לכתוב את {% equation %}\left|\psi\right\rangle {% endequation %} בצורה פשוטה בתור וקטור: {% equation %}\left|\psi\right\rangle =\left(\begin{array}{c} \alpha\\ \beta \end{array}\right){% endequation %}. עכשיו, את {% equation %}\left\langle \psi\right|{% endequation %} הגדרתי אי שם בפוסט הראשון שלי בנושא: זה פשוט הצמוד ההרמיטי של {% equation %}\left|\psi\right\rangle {% endequation %}, כלומר זה וקטור השורה {% equation %}\left(\begin{array}{cc} \overline{\alpha} & \overline{\beta}\end{array}\right){% endequation %}. כמו כן כבר ראינו ש-{% equation %}M_{0}^{\dagger}M_{0}=M_{0}{% endequation %}, אז הביטוי {% equation %}\left\langle \psi\right|M_{0}^{\dagger}M_{0}\left|\psi\right\rangle {% endequation %} הוא בסך הכל החישוב הפשוט למדי

{% equation %}\left(\begin{array}{cc} \overline{\alpha} & \overline{\beta}\end{array}\right)\left(\begin{array}{cc} 1 & 0\\ 0 & 0 \end{array}\right)\left(\begin{array}{c} \alpha\\ \beta \end{array}\right)=\left(\begin{array}{cc} \overline{\alpha} & \overline{\beta}\end{array}\right)\left(\begin{array}{c} \alpha\\ 0 \end{array}\right)=\left|\alpha\right|^{2}{% endequation %}

בדיוק המספר שציפינו לקבל, וגם {% equation %}\left|\beta\right|^{2}{% endequation %} מתקבל בצורה דומה.

אם 0 עלה בגורל, אנחנו הולכים לעבור למצב {% equation %}M_{0}\left|\psi\right\rangle {% endequation %} אחרי נירמול. המצב הזה לפני נירמול הוא {% equation %}\left(\begin{array}{cc} 1 & 0\\ 0 & 0 \end{array}\right)\left(\begin{array}{c} \alpha\\ \beta \end{array}\right)=\left(\begin{array}{c} \alpha\\ 0 \end{array}\right){% endequation %}. בשביל לנרמל, צריך לחשב את הנורמה של המצב. אני רוצה לטעון שהנורמה הזו היא בדיוק {% equation %}\sqrt{\left\langle \psi\right|M_{0}^{\dagger}M_{0}\left|\psi\right\rangle }{% endequation %}. למה? ובכן, זכרו איך נורמה של וקטור כלשהו {% equation %}v{% endequation %} מוגדרת:

{% equation %}\|v\|=\sqrt{\left\langle v|v\right\rangle }{% endequation %}

זכרו גם שאצלנו, אם {% equation %}\left|\psi\right\rangle ,\left|\phi\right\rangle {% endequation %} הם שני וקטורים, המכפלה הפנימית שלהם שווה ל-{% equation %}\left\langle \phi\right|\left|\psi\right\rangle {% endequation %}. לבסוף, שימו לב שאם {% equation %}\left|\phi\right\rangle =M_{0}\left|\psi\right\rangle {% endequation %} אז {% equation %}\left\langle \phi\right|=\left\langle \psi\right|M_{0}^{\dagger}{% endequation %}. למה? ובכן, זה מצריך לזכור משהו קטן מאלגברה לינארית: שאם {% equation %}A,B{% endequation %} הן שתי מטריצות כלשהן, אז

{% equation %}\left(AB\right)^{\dagger}=B^{\dagger}A^{\dagger}{% endequation %}

במקרה שלנו, שתי המטריצות הן {% equation %}M_{0}\left|\psi\right\rangle {% endequation %}. אם כן, בביטוי {% equation %}p\left(0\right)=\left\langle \psi\right|M_{0}^{\dagger}M_{0}\left|\psi\right\rangle {% endequation %}, ההסתברות היא בדיוק הנורמה של המצב {% equation %}M_{0}\left|\psi\right\rangle {% endequation %} שאליו (אחרי נרמול) אנחנו רוצים להעביר את {% equation %}\left|\psi\right\rangle {% endequation %}, והאופרטור {% equation %}M_{0}{% endequation %} בעצם אומר לנו <strong>לאן</strong> מצבים אמורים לעבור כשמודדים אותם.

השאלה שעדיין תלויה בחלל האוויר היא "למה זה עובד?". לא לגמרי ברור מה אמור <strong>לא לעבוד</strong> כאן, אבל הרי לא דרשתי את התנאי {% equation %}\sum_{i=0}^{k-1}M_{i}^{\dagger}M_{i}=I{% endequation %} סתם, הוא בא להשיג מטרה כלשהי. המטרה פשוטה: להראות שה-{% equation %}p\left(i\right){% endequation %}-ים שלי אכן מהווים הסתברות.

מה הדרישות המתמטיות מפונקציית הסתברות?

<ol> <li>שלכל תוצאה אפשרית {% equation %}i{% endequation %} יתקיים {% equation %}0\le p\left(i\right)\le1{% endequation %}</li>


<li>שסכום כל ההסתברויות יהיה 1: {% equation %}\sum_{i=0}^{k-1}p\left(i\right)=1{% endequation %}.</li>

</ol>

כמובן, מספיק להראות ש-{% equation %}0\le p\left(i\right){% endequation %} ושסכום ההסתברויות יוצא 1 כדי להבטיח שיתקיים {% equation %}p\left(i\right)\le1{% endequation %} (כי אם סכום של מספרים אי-שליליים הוא 1, לא ייתכן שאחד מהאיברים בסכום גדול מ-1).

מכיוון שראינו ש-{% equation %}p\left(i\right)=\left\langle \psi\right|M_{i}^{\dagger}M_{i}\left|\psi\right\rangle {% endequation %} הוא מכפלה פנימית, ברור ש-{% equation %}p\left(i\right)\ge0{% endequation %} - זה שמכפלה פנימית של איבר בעצמו היא אי-שלילית זו אחת מהדרישות הבסיסיות ביותר ממכפלה פנימית. נשאר רק עניין הסכום, וכאן נלחצת לעזרתנו העובדה שבאלגברה לינארית הכל לינארי, ושהביטוי {% equation %}\left\langle \psi\right|M_{i}^{\dagger}M_{i}\left|\psi\right\rangle {% endequation %} אולי נראה מפחיד אבל הוא בסך הכל מכפלה של ארבע מטריצות ולכן כפוף לחוקי הלינאריות, ומתקיים

{% equation %}\sum_{i=0}^{k-1}p\left(i\right)=\sum_{i=0}^{k-1}\left\langle \psi\right|M_{i}^{\dagger}M_{i}\left|\psi\right\rangle ={% endequation %}

{% equation %}=\left\langle \psi\right|\left(\sum_{i=0}^{k-1}M_{i}^{\dagger}M_{i}\right)\left|\psi\right\rangle =\left\langle \psi\right|I\left|\psi\right\rangle =\left\langle \psi|\psi\right\rangle =1{% endequation %}

כשהמעבר האחרון נובע מכך ש-{% equation %}\left|\psi\right\rangle {% endequation %} הוא מנורמה 1. בסך הכל פשוט מאוד!

<h2>מדידות, באופן קצת פחות כללי</h2>

ההגדרה של מדידות שנתתי עשויה להרגיש <strong>יותר מדי</strong> כללית, ולא לגמרי ברור מאיפה סדרת ה-{% equation %}M{% endequation %}-ים מגיעה. אז אני הולך לדבר עכשיו על משפחה קצת יותר מצומצמת של מדידות - כאלו שמתקבלות מ<strong>אופרטור הרמיטי</strong>.

באלגברה לינארית, אופרטור {% equation %}\mathcal{H}{% endequation %} הוא <strong>הרמיטי</strong> (או <strong>צמוד לעצמו</strong>)<strong> </strong>אם {% equation %}\mathcal{H}^{\dagger}=\mathcal{H}{% endequation %}. בהגדרה שקולה: אם {% equation %}\left\langle \mathcal{H}v,u\right\rangle =\left\langle v,\mathcal{H}u\right\rangle {% endequation %} לכל {% equation %}v,u{% endequation %}. אופרטורים הרמיטיים הם יצורים נחמדים במיוחד. אפשר לחשוב עליהם בתוך קבוצת כל האופרטורים בערך כמו שאפשר לחשוב על הממשיים כחלק מקבוצת כל המרוכבים (למשל כל אופרטור מעל המרוכבים אפשר לכתוב כסכום {% equation %}H_{1}+iH_{2}{% endequation %} של אופרטורים הרמיטיים {% equation %}H_{1},H_{2}{% endequation %}, קצת בדומה לכתיב {% equation %}a+bi{% endequation %} של מרוכבים), אבל לא ניכנס לזה יותר מדי כאן. אבל לאופרטורים הרמיטיים יש כמה תכונות נחמדות שכן כדאי לציין:

<ul> <li>כל הערכים העצמיים של אופרטור הרמיטים הם <strong>ממשיים</strong>. קל לראות את זה, כי אם {% equation %}\mathcal{H}v=\lambda v{% endequation %} אז {% equation %}\left\langle \mathcal{H}v|v\right\rangle =\left\langle \lambda v|v\right\rangle =\|v\|^{2}\overline{\lambda}{% endequation %} מחד, אבל {% equation %}\left\langle \mathcal{H}v|v\right\rangle =\left\langle v|\mathcal{H}v\right\rangle =\left\langle v,\lambda v\right\rangle =\|v\|^{2}\lambda{% endequation %}, ולכן {% equation %}\lambda=\overline{\lambda}{% endequation %}.</li>


<li>וקטורים עצמיים ששייכים לערכים עצמיים שונים הם <strong>אורתוגונליים</strong>, כלומר המכפלה הפנימית שלהם היא 0. הטריק שמראה את זה דומה למה שראינו קודם: אם {% equation %}v,u{% endequation %} מתאימים לערכים העצמיים השונים {% equation %}\lambda,\rho{% endequation %} אז {% equation %}\lambda\left\langle v|u\right\rangle =\left\langle \mathcal{H}v|u\right\rangle =\left\langle v|\mathcal{H}u\right\rangle =\rho\left\langle v|u\right\rangle {% endequation %} ולכן {% equation %}\left(\lambda-\rho\right)\left\langle v|u\right\rangle =0{% endequation %} ומכיוון ש-{% equation %}\lambda\ne\rho{% endequation %} זה מכריח את {% equation %}\left\langle v|u\right\rangle =0{% endequation %}.</li>

</ul>

מאלו מקבלים, עם עוד קצת עבודה טכנית, שאפשר לקבל בסיס אורתונורמלי למרחב ש-{% equation %}\mathcal{H}{% endequation %} פועלת עליו שכולו מורכב מוקטורים עצמיים של {% equation %}\mathcal{H}{% endequation %}. זה יותר מ"סתם" לכסון, בזכות העובדה שהוקטורים העצמיים הם אורתוגונליים. השורה התחתונה של זה, שהיא מה שיעניין אותנו כאן, היא שיש ל-{% equation %}\mathcal{H}{% endequation %} מה שנקרא <strong>פירוק ספקטרלי</strong> - דרך להציג אותה בתור סכום

{% equation %}\mathcal{H}=\lambda_{1}P_{1}+\ldots+\lambda_{k}P_{k}{% endequation %}

כאשר {% equation %}\lambda_{1},\ldots,\lambda_{k}{% endequation %} הם הערכים העצמיים השונים של {% equation %}\mathcal{H}{% endequation %}, ו-{% equation %}P_{i}{% endequation %} היא <strong>הטלה אורתוגונלית</strong> למרחב העצמי של {% equation %}\lambda_{i}{% endequation %}, כלומר למרחב שנפרש על ידי כל הוקטורים העצמיים של {% equation %}\mathcal{H}{% endequation %} שמתאימים לערך העצמי {% equation %}\lambda_{i}{% endequation %}.

איך כל זה קשור למדידות? ובכן, תחשבו על {% equation %}\mathcal{H}{% endequation %} בתור אופרטור שמקודד בתוכו את המידע השלם של מדידה מסוימת. הערכים {% equation %}\lambda_{1},\ldots,\lambda_{k}{% endequation %} הם התוצאות האפשריות של המדידה הזו (תוצאות מספריות שמתבטאות במספרים ממשיים; תחשבו על מדידות של מהירות, מיקום וכדומה). האופרטורים {% equation %}P_{1},\ldots,P_{k}{% endequation %} שמטילים למרחב העצמי המתאים הם אופרטורי המדידה שלנו, מה שקראתי לו {% equation %}M{% endequation %} קודם.

אני לא ארחיב כאן יותר מדי על מה זו הטלה אורתוגונלית, אבל מה שרלוונטי לענייננו הוא שאם {% equation %}P{% endequation %} היא הטלה כזו אז היא הרמיטית, כלומר {% equation %}P^{\dagger}=P{% endequation %}, וכמו כן {% equation %}P^{2}=P{% endequation %}, כך שיוצא ש-{% equation %}P^{\dagger}P=P{% endequation %}. לכן, כדי לראות שה-{% equation %}P{% endequation %}-ים ש-{% equation %}\mathcal{H}{% endequation %} נתן לנו מגדירים מדידה חוקית, מספיק להראות שמתקיים

{% equation %}\sum_{i=0}^{k-1}P_{i}=I{% endequation %}

זה נובע בקלות מהמשוואה {% equation %}\mathcal{H}=\lambda_{1}P_{1}+\ldots+\lambda_{k}P_{k}{% endequation %}. אם מפעילים פולינום {% equation %}p{% endequation %} כלשהו על המשוואה הזו, אז בזכות העובדה שוקטורים עצמיים שונים הם אורתוגונליים, שמובילה לכך ש-{% equation %}P_{i}P_{j}=0{% endequation %} לכל {% equation %}i\ne j{% endequation %}, מקבלים

{% equation %}p\left(\mathcal{H}\right)=p\left(\lambda_{1}\right)P_{1}+\ldots+p\left(\lambda_{k}\right)P_{k}{% endequation %}

ובפרט עבור {% equation %}p=1{% endequation %} מקבלים {% equation %}P_{1}+\ldots+P_{k}=I{% endequation %}, שזה מה שרצינו.

כרגיל, כדאי לראות דוגמאות. אילו אופרטורים הרמיטיים אנחנו מכירים? ראינו שניים פשוטים למדי שפועלים על מרחב של קיוביט בודד:

{% equation %}Z=\left(\begin{array}{cc} 1 & 0\\ 0 & -1 \end{array}\right){% endequation %}

{% equation %}X=\left(\begin{array}{cc} 0 & 1\\ 1 & 0 \end{array}\right){% endequation %}

בשביל {% equation %}Z{% endequation %} מאוד קל למצוא פירוק ספקטרלי - הוא כבר כך לכסין. והוקטורים העצמיים שלו הם פשוט {% equation %}\left(\begin{array}{c} 1\\ 0 \end{array}\right){% endequation %} ו-{% equation %}\left(\begin{array}{c} 0\\ 1 \end{array}\right){% endequation %} או בסימונים הקוונטיים שלנו, {% equation %}\left|0\right\rangle {% endequation %} ו-{% equation %}\left|1\right\rangle {% endequation %}. שימו לב ש-{% equation %}Z{% endequation %} עצמו <strong>לא</strong> מהווה מדידה! זה אופרטור אוניטרי נחמד שאפשר להשתמש בו במהלך חישוב רגיל. המדידה נכנסת לתמונה כשאנחנו לוקחים את <strong>הפירוק הספקטרלי</strong> של {% equation %}Z{% endequation %}, שהוא פשוט:

{% equation %}Z=\left(+1\right)\left(\begin{array}{cc} 1 & 0\\ 0 & 0 \end{array}\right)+\left(-1\right)\left(\begin{array}{cc} 0 & 0\\ 0 & 1 \end{array}\right){% endequation %}

כבר ראינו את שתי המטריצות הללו קודם, בדוגמא שנתתי לאיך מדידה "רגילה" תואמת את ההגדרה באמצעות אופרטורים. עכשיו קיבלנו דרך יותר טבעית לקבל את שתיהן, וגם ראינו שבמקום להצמיד להן תגיות שהן המחרוזת "0" והמחרוזת "1" אפשר להצמיד להן את התגיות המספריות {% equation %}\pm1{% endequation %}. לרוב אני אדבוק בתגיות של "0" ו-\textquotedblleft1" בכל זאת, אבל כדאי להכיר גם את הגישה השניה. לפעמים כשמדברים על "מדידה רגילה" אומרים "מדידה בבסיס {% equation %}Z{% endequation %}"; עכשיו אפשר להבין מאיפה ה-{% equation %}Z{% endequation %} הזה מגיע.

אם זו הייתה מדידה בבסיס {% equation %}Z{% endequation %}, מה זו מדידה בבסיס {% equation %}X{% endequation %}? כבר ראינו בפוסט קודם שמתקיים

{% equation %}X\left|+\right\rangle =\left|+\right\rangle {% endequation %}

{% equation %}X\left|-\right\rangle =-\left|-\right\rangle {% endequation %}

כלומר, עבור {% equation %}X{% endequation %} הוקטורים העצמיים הם {% equation %}\left|+\right\rangle ,\left|-\right\rangle {% endequation %}, עם הערכים העצמיים {% equation %}\pm1{% endequation %} (כמו עבור {% equation %}Z{% endequation %}), ועם קצת עבודה אפשר לראות שהפירוק הספקטרלי הוא

{% equation %}X=\left(+1\right)\left(\begin{array}{cc} \frac{1}{2} & \frac{1}{2}\\ \frac{1}{2} & \frac{1}{2} \end{array}\right)+\left(-1\right)\left(\begin{array}{cc} \frac{1}{2} & -\frac{1}{2}\\ -\frac{1}{2} & \frac{1}{2} \end{array}\right){% endequation %}

המטריצות הללו הן {% equation %}\left|+\right\rangle \left\langle +\right|{% endequation %} ו-{% equation %}\left|-\right\rangle \left\langle -\right|{% endequation %} אם תהיתם מהיכן הן צצו.

זוכרים את השוויון {% equation %}HZH=X{% endequation %} שראינו פעם? בגלל שבפירוק הספקטרלי הכל לינארי, במקום למדוד בבסיס {% equation %}X{% endequation %} אפשר לעשות את התעלול הבא: להפעיל {% equation %}H{% endequation %}, למדוד בבסיס {% equation %}Z{% endequation %}, להפעיל {% equation %}H{% endequation %} שוב על המצב שהגענו אליו, וכך "לסמלץ" את המדידה בבסיס {% equation %}X{% endequation %} - המצב שנגיע אליו בסוף הוא זה שהיינו מגיעים אליו אם היינו מודדים בבסיס {% equation %}X{% endequation %}, וגם הערך שהמדידה החזירה ({% equation %}\pm1{% endequation %}) מתאים למה שהיינו רואים אם היינו מודדים בבסיס {% equation %}X{% endequation %}.

<h2>מדידות, במובן המאוד פרטני שאנחנו ממש ממש צריכים כדי להמשיך</h2>

קשקשתי כל כך הרבה בפוסט הזה. האם עניתי על השאלה הבסיסית? השאלה "מה קורה אם יש לי שני קיוביטים ואני מודד רק אחד מהם?" ובכן, בתיאוריה כן, כי נתתי תשובה מאוד כללית, אבל מה קורה בפועל?

אמרתי שמדידה רגילה מתוארת על ידי הפירוק הספקטרלי של {% equation %}Z{% endequation %}, וסימנתי את המטריצות המתאימות ב-{% equation %}M_{0}=\left(\begin{array}{cc} 1 & 0\\ 0 & 0 \end{array}\right),M_{1}=\left(\begin{array}{cc} 0 & 0\\ 0 & 1 \end{array}\right){% endequation %} (שימו לב שהשתמשתי כאן בסימון המקורי ולא בזה של ההטלות). אז מדידה של הקיוביט הראשון, בלי שינוי של השני, מתוארת על ידי הפירוק הספקטרלי של {% equation %}Z\otimes I{% endequation %}. כלומר, המטריצות שמגדירות את המדידה הן

{% equation %}M_{0}\otimes I{% endequation %}

{% equation %}M_{1}\otimes I{% endequation %}

מה ש-{% equation %}M_{0}{% endequation %} עושה הוא פשוט:

{% equation %}M_{0}\left|0\right\rangle =\left|0\right\rangle {% endequation %}

{% equation %}M_{0}\left|1\right\rangle =0{% endequation %}

שימו לב: בשורה השניה זה לא הקיוביט {% equation %}\left|0\right\rangle {% endequation %} מצד ימין. זה 0. המספר 0. וקטור האפס. כלום. נאדה, גורנישט. דבר כזה יכול להתקבל כי {% equation %}M_{0}{% endequation %} הוא הטלה; הוא לא אופרטור אוניטרי ולא צריך להיות הפיך.

באופן דומה, {% equation %}\left(\begin{array}{cc} 0 & 0\\ 0 & 1 \end{array}\right){% endequation %} מאפס את {% equation %}\left|0\right\rangle {% endequation %} ומשאיר ללא שינוי את {% equation %}\left|1\right\rangle {% endequation %}. זה מאפשר לנו להבין מה האופרטורים הללו עושים כשמטנזרים אותם עם {% equation %}I{% endequation %}: {% equation %}M_{0}\otimes I{% endequation %} הולך להשאיר ללא שינוי את {% equation %}\left|00\right\rangle ,\left|01\right\rangle {% endequation %} ולאפס את שני האחרים, ו-{% equation %}M_{1}{% endequation %} יעשה ההפך. כלומר נקבל את האפקט הבא על מצב כללי, {% equation %}\alpha\left|00\right\rangle +\beta\left|01\right\rangle +\gamma\left|10\right\rangle +\delta\left|11\right\rangle {% endequation %}:

{% equation %}M_{0}\left(\alpha\left|00\right\rangle +\beta\left|01\right\rangle +\gamma\left|10\right\rangle +\delta\left|11\right\rangle \right)=\alpha\left|00\right\rangle +\beta\left|01\right\rangle {% endequation %}

{% equation %}M_{1}\left(\alpha\left|00\right\rangle +\beta\left|01\right\rangle +\gamma\left|10\right\rangle +\delta\left|11\right\rangle \right)=\gamma\left|10\right\rangle +\delta\left|11\right\rangle {% endequation %}

אם נחזור לתחילת הפוסט, נראה שזה מה שעשיתי כבר אז, אבל קראתי לזה נפנופי ידיים. האם עכשיו זה מרגיש יותר פורמלי? ובכן... אני מקווה.

יש נקודה נוספת שעדיין לא התייחסתי אליה והיא די מעצבנת - כדי לדעת מה ההסתברות ש-0 ייבחר, לא מספיק להפעיל את {% equation %}M_{0}{% endequation %} על המצב הכללי ולקבל את {% equation %}\alpha\left|00\right\rangle +\beta\left|01\right\rangle {% endequation %}, צריך גם לחשב את המכפלה הפנימית של הוקטור הזה בעצמו. איך עושים את זה בקלות? ובכן, הרעיון הוא לקחת את הוקטור וקודם כל לחשב את הצמוד ההרמיטי שלו. היתרון בשיטת הסימון שלנו הוא שזה כרוך בשני דברים בלבד: להצמיד את הסקלרים, ולהפוך את הכיוון של הסוגריים:

{% equation %}\overline{\alpha}\left\langle 00\right|+\overline{\beta}\left\langle 01\right|{% endequation %}

עכשיו אפשר לכפול בצורה שבה מתבצע כפל רגיל:

{% equation %}\left(\overline{\alpha}\left\langle 00\right|+\overline{\beta}\left\langle 01\right|\right)\left(\alpha\left|00\right\rangle +\beta\left|01\right\rangle \right)={% endequation %}

{% equation %}=\left|\alpha\right|^{2}\left\langle 00\right|\left|00\right\rangle +\overline{\alpha}\beta\left\langle 00\right|\left|01\right\rangle +\alpha\overline{\beta}\left\langle 01\right|\left|00\right\rangle +\left|\beta\right|^{2}\left\langle 01\right|\left|01\right\rangle {% endequation %}

בבירור {% equation %}\left\langle 00\right|\left|00\right\rangle =\left\langle 01\right|\left|01\right\rangle =1{% endequation %} כי זו מכפלה פנימית של וקטור מנורמה 1 בעצמו. אבל מה זה {% equation %}\left\langle 00\right|\left|01\right\rangle {% endequation %} למשל? ובכן, עד עכשיו לא ממש הסברתי איך אנחנו מגדירים מכפלה פנימית על מרחב שהוא מכפלה טנזורית, אבל אני לא חושב שמפתיע במיוחד שההגדרה המקובלת היא

{% equation %}\left\langle u_{1}\otimes w_{1}|u_{2}\otimes w_{2}\right\rangle =\left\langle u_{1}|u_{2}\right\rangle \cdot\left\langle w_{1}|w_{2}\right\rangle {% endequation %}

ולכן, בסימונים שלנו:

{% equation %}\left\langle 00\right|\left|01\right\rangle =\left\langle 0\right|\left|0\right\rangle \cdot\left\langle 0\right|\left|1\right\rangle {% endequation %}

ומכיוון ש-{% equation %}\left\langle 0\right|\left|1\right\rangle =0{% endequation %} כי אלו וקטורים אורתוגונליים, נקבל {% equation %}\left\langle 00\right|\left|01\right\rangle =0{% endequation %}. וכך גם באופן כללי: אם {% equation %}x\ne y{% endequation %} הם שניהם מחרוזות ב-{% equation %}\left\{ 0,1\right\} ^{n}{% endequation %} אז {% equation %}\left\langle x\right|\left|y\right\rangle =0{% endequation %}. לכן קיבלנו שהמכפלה הפנימית של {% equation %}\alpha\left|00\right\rangle +\beta\left|01\right\rangle {% endequation %} בעצמו היא {% equation %}\left|\alpha\right|^{2}+\left|\beta\right|^{2}{% endequation %}, כפי שנפנפתי בידיים בתחילת הפוסט.

האם סיימנו? אני מקווה שכן! כלומר, יש לנו את כל הכלים המתמטיים שצריך כדי להתחיל להראות חישובים קוונטיים אמתיים ולהבין מה קורה בהם; את זה נתחיל בפוסט הבא. 
