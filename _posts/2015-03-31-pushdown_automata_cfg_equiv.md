---
id: 3233
title: "שקילות אוטומט מחסנית ודקדוק חסר הקשר"
date: 2015-03-31 13:04:13
layout: post
categories: 
  - תורת הסיבוכיות
tags: 
  - אוטומט מחסנית
  - דקדוק חסר הקשר
  - שפות חסרות הקשר
  - שפות פורמליות
---
<a href="http://www.gadial.net/2015/03/22/pushdown_automata/">בפוסט הקודם</a> הצגתי את המודל של <strong>אוטומט מחסנית</strong>. המטרה הייתה להציג מודל של אוטומט שמחלקת השפות שמתאימה לו היא בדיוק מחלקת השפות חסרות ההקשר. לצורך זה, חשבתי על אלגוריתם פשוט לזיהוי שפה של דקדוק חסר הקשר כלשהו, ואז לקחתי מודל של אוטומט שמסוגל לממש בקלות את האלגוריתם הזה. בכך הוכחתי את הכיוון ה"קל" - שאוטומט מחסנית מקבל כל שפה חסרת הקשר. עכשיו הגיע הזמן לכיוון הקשה יותר - שהשפה של אוטומט מחסנית היא תמיד חסרת הקשר - דהיינו, שבהינתן אוטומט מחסנית {% equation %}M{% endequation %} קיים דקדוק חסר הקשר {% equation %}G{% endequation %} כך ש-{% equation %}L\left(G\right)=L\left(M\right){% endequation %}. זה קשה, כי אנחנו צריכים איכשהו "לסמלץ" אוטומט עם דקדוק, מה שנראה לא קשור בעליל במבט ראשון ואכן ידרוש מאיתנו בניה חכמה למדי - כנראה הדבר הכי מסובך שראינו עד כה בסדרת הפוסטים על שפות פורמליות, אבל עדיין לא משהו <strong>עד כדי כך</strong> מסובך, לא לדאוג.

בואו ניסגר מראש על הפורמליסטיקה. ניקח אוטומט מחסנית {% equation %}M=\left(Q,\Sigma,\Gamma,q_{0},\bot,\delta,\emptyset\right){% endequation %} עם קבוצת מצבים {% equation %}Q{% endequation %}, א"ב קלט ומחסנית {% equation %}\Sigma,\Gamma{% endequation %} בהתאמה, מצב התחלתי {% equation %}q_{0}{% endequation %} וסימן תחתית מחסנית {% equation %}\bot{% endequation %} ופונקציית מעברים {% equation %}\delta{% endequation %}, כך ש-{% equation %}\delta\left(q,\sigma,A\right){% endequation %}, עבור {% equation %}\sigma\in\Sigma\cup\left\{ \varepsilon\right\} {% endequation %} ו-{% equation %}A\in\Gamma{% endequation %}, היא קבוצה של זוגות {% equation %}\left(p,\beta\right){% endequation %} שפירושם "במצב {% equation %}q{% endequation %} אחרי קריאת {% equation %}\sigma{% endequation %} ועם {% equation %}A{% endequation %} בראש המחסנית אפשר לעבור למצב {% equation %}p{% endequation %} ולדחוף {% equation %}\beta{% endequation %} במקום {% equation %}A{% endequation %}". קבוצת המצבים המקבלים תהיה ריקה כי אני אתעניין רק באוטומט שמקבל על ידי ריקון (לכל אוטומט שמקבל על ידי מצבים מקבלים יש אוטומט שקול שמקבל על ידי ריקון). כלומר, שפת האוטומט מוגדרת כך:

{% equation %}L\left(M\right)=\left\{ w\in\Sigma^{*}\ |\ \exists p\in Q:\left[q_{0},w,\bot\right]\vdash^{*}\left[p,\varepsilon,\varepsilon\right]\right\} {% endequation %}

כאשר {% equation %}\left[q,w,\alpha\right]{% endequation %} היא <strong>קונפיגורציה</strong> של האוטומט שמתארת את המצב הנוכחי {% equation %}q{% endequation %}, הקלט שנותר {% equation %}w{% endequation %} ותוכן המחסנית {% equation %}\alpha{% endequation %}, והסימן {% equation %}\vdash^{*}{% endequation %} אומר "אפשר לעבור מהקונפיגורציה השמאלית לימנית ב-0 או יותר צעדים".

עכשיו, איך ניגשים לבניה שלנו? במבט ראשון זה נראה מפחיד ואין לנו מושג מאיפה להתחיל, כי דקדוק זה משהו שמייצר מילים על ידי כך שהוא משליך הרבה אותיות לפה ולשם ופתאום יש מילה מוגמרת, ולעומת זאת אוטומט עובר סדרתית על אותיות ועושה חישובים וכדומה. אבל בעצם, אם חושבים על זה, כבר ראינו משהו דומה - דקדוק שמסמלץ אוטומט סופי דטרמיניסטי. שם הרעיון היה כזה: משתני הדקדוק היו {% equation %}Q{% endequation %}, הטרמינלים היו {% equation %}\Sigma{% endequation %} ולכל מעבר {% equation %}\delta\left(q,\sigma\right)=p{% endequation %} היה לנו את כלל הגזירה {% equation %}q\to\sigma p{% endequation %}. כך הדקדוק יצר את המילה "אות אחרי אות" כשהסימן הימני ביותר בתבנית הפסוקית שבמהלך הבניה תמיד תיאר את המצב הנוכחי של האוטומט - בעצם, אם חושבים על זה, זה סוג של תיאור של ה<strong>קונפיגורציה</strong> שלו (רק בלי "מה שנשאר מהקלט").

אז למה לא לעשות בניה דומה עבור אוטומט מחסנית? הרי ההבדל היחיד הוא שעכשיו יש לנו גם מחסנית. למה לא לתאר את הקונפיגורציה הנוכחית של האוטומט בלי שארית הקלט בתור זוג {% equation %}\left(q,\alpha\right){% endequation %} כאשר {% equation %}\alpha\in\Gamma^{*}{% endequation %} ולכל מעבר {% equation %}\left(p,\beta\right)\in\delta\left(q,\sigma,A\right){% endequation %} להוסיף את הגזירה הבאה בדקדוק: {% equation %}\left(q,A\alpha\right)\to\sigma\left(p,\beta\alpha\right){% endequation %}?

התשובה פשוטה מאוד - כי הדקדוק שנקבל יהיה בעל <strong>אינסוף משתנים</strong> - כי הרי יש לנו אינסוף זוגות {% equation %}\left(q,\alpha\right){% endequation %} עם {% equation %}\alpha\in\Gamma^{*}{% endequation %} שהרי הגודל של המחסנית של האוטומט לא חסום. הכשלון הזה לא מפתיע במיוחד כי אם הוא היה מצליח, מה שהיינו בונים הוא <strong>דקדוק לינארי ימני</strong>, מה שהיה מוכיח שהשפה שלנו היא בכלל רגולרית, דהיינו היינו מוכיחים שכל שפה חסרת הקשר היא רגולרית, וזה בוודאי לא נכון. אם כן, אין לנו תקווה לדקדוק שיהיה <strong>עד כדי כך</strong> פשוט.

עדיין, מה שעשינו הוא התחלה טובה שתוביל אותנו בסופו של דבר אל הבניה שעובדת. בואו ננסה להציע לה תיקון נאיבי ונראה מה יקרה: מכיוון שהבעיה שלנו היא עם כך ש-{% equation %}\alpha{% endequation %} הוא לא חסום באורכו, הנה הצעה: פשוט נפרוט אותו לפרוטות. נוסיף את כל {% equation %}\Gamma{% endequation %} לקבוצת המשתנים של הדקדוק שלנו, ועכשיו תבנית פסוקית אופיינית תיראה, נאמר, כך: {% equation %}aabqABB{% endequation %}. התבנית הזו אומרת "עד כה הסימולציה של האוטומט שלנו קראה את {% equation %}aab{% endequation %}; עכשיו אנחנו במצב {% equation %}q{% endequation %}; תוכן המחסנית הוא {% equation %}ABB{% endequation %}". זה נראה מאוד מבטיח כי האוטומט פועל רק על פי התו העליון במחסנית, שממילא צמוד ל-{% equation %}q{% endequation %}, אז נראה שאפשר לעשות כאן משהו.

למה הבניה הזו נכשלת? כי הדקדוק שלנו צריך להיות <strong>חסר הקשר</strong>. כאשר אני גוזר את המשתנה {% equation %}q{% endequation %}, המשתנה לא יודע מי נמצא מימינו ומשמאלו והגזירה לא תהיה מושפעת מזה. במילים אחרות, אין ל-{% equation %}q{% endequation %} דרך "להכיר" את ה-{% equation %}A{% endequation %} שמימינו. תגידו, אוקיי - בואו נחבר את שניהם מראש לזוג, כלומר התבנית תיראה כך: {% equation %}aab\left(q,A\right)BB{% endequation %}. זה טוב ויפה, אבל אחרי ש-{% equation %}\left(q,A\right){% endequation %} נגזר למשהו, איך אותו משהו יתחבר אל ה-{% equation %}B{% endequation %}-ים שמשמאל?

בקיצור, גם זה לא יעבוד. אני לא יכול שיהיו לי משתנים שהם "מצב לבד" ו"אות מחסנית לבד" - אני חייב שהמשתנים שלי יכללו מידע גם עבור המצב וגם עבור האות במחסנית. איך נעשה את זה? בואו ננסה פשוט לחבר אותם לזוגות ונראה איך זה עובד בדוגמה שלעיל: {% equation %}\left(q_{3},B\right){% endequation %}{% equation %}aab\left(q_{1},A\right)\left(q_{2},B\right){% endequation %}. כאשר כאן {% equation %}q_{1},q_{2},q_{3}{% endequation %} הם מצבים כלשהם. מה שאני מצפה מ-{% equation %}\left(q_{1},A\right){% endequation %} לגזור זה את "החלק במילה שעליו האוטומט רץ עד לשלב שבו הוא מגיע למצב {% equation %}q_{2}{% endequation %} ובמחסנית נשארו רק {% equation %}BB{% endequation %}", ומה שאני מצפה מ-{% equation %}\left(q_{2},B\right){% endequation %} לגזור זה את "החלק במילה שעליו האוטומט רץ עד לשלב שבו הוא מגיע למצב {% equation %}q_{3}{% endequation %} ובמחסנית נשאר רק {% equation %}B{% endequation %}" ו-{% equation %}\left(q_{3},B\right){% endequation %} אמור לגזור את "החלק המילה שעליו האוטומט רץ עד שהמחסנית מתרוקנת". משהו כאן עדיין לא עובד, אבל אני חושב שאנחנו כבר רואים שזה מתחמם ואנחנו מתקרבים לבניה שתעבוד.

הבעיה בבניה הנוכחית היא שהיא עדיין תלוית הקשר במובן מסויים - מה זאת אומרת, אני מצפה מ-{% equation %}\left(q_{1},A\right){% endequation %} לגזור את החלק במילה שעליו האוטומט רץ עד שהוא מגיע ל-{% equation %}q_{2}{% endequation %} ובמחסנית יש {% equation %}BB{% endequation %}? איך הוא יודע מ-{% equation %}q_{2}{% endequation %} ומ-{% equation %}BB{% endequation %}? כרגע הוא לא. אבל שימו לב - הוא בעצם לא באמת מתעניין ב-{% equation %}BB{% endequation %}. אפשר לנסח את זה מחדש: {% equation %}\left(q_{1},A\right){% endequation %} אמור לגזור את החלק במילה שעליו האוטומט רץ עד שהוא מגיע ל-{% equation %}q_{2}{% endequation %} והמחסנית מגיעה למצב שבו מה שהיה מתחת ל-{% equation %}A{% endequation %} נחשף לראשונה. הקטע הזה עם ה"נחשף לראשונה" נראה לי כמו הדבר הכי מבלבל כאן, אז בואו נפרט קצת: על פי ההגדרה שלו, הדבר הראשון שהאוטומט עושה כשהוא מבצע צעד זה להסיר את {% equation %}A{% endequation %} מהמחסנית. אבל מייד אחר כך הוא דוחף במקום {% equation %}A{% endequation %} מילה {% equation %}\beta{% endequation %} כלשהי. אם {% equation %}\beta{% endequation %} היא המילה הריקה, אז מה שהיה מתחת ל-{% equation %}A{% endequation %} נחשף; אחרת, {% equation %}A{% endequation %} הוחלף על ידי תווים נוספים (אולי יותר מ-1) ומה שהיה קבור מתחת ל-{% equation %}A{% endequation %} נשאר קבור ונצטרך לטפל בכל מה שמעליו לפני שנגיע אליו.

אם כן, לא באמת אכפת לנו מה-{% equation %}BB{% endequation %}, אבל כן אכפת לנו מ-{% equation %}q_{2}{% endequation %}. אבל כאן אין בעצם בעיה, כי {% equation %}q_{2}{% endequation %} הוא מצב בודד ואפשר לזכור אותו - זו כבר לא סדרה בלתי חסומה של תווים. זה מוביל אותנו אל הרעיון שמאחורי הבניה האמיתית שבה נשתמש: המשתנים שלנו יהיו שלשות {% equation %}\left(q,A,p\right){% endequation %} כך שהמילים ששלשות כאלו גוזרות הן בדיוק המילים שמאפשרות לאוטומט לעבור מ-{% equation %}q{% endequation %} אל {% equation %}p{% endequation %} כאשר בהתחלה {% equation %}A{% endequation %} בראש המחסנית ובסיום נחשף מה שהיה מתחתיו.

בואו נכתוב את זה בצורה פורמלית. אני רוצה לבנות את הדקדוק בצורה כזו שיתקיים הדבר הבא:

{% equation %}\left(q,A,p\right)\Rightarrow^{*}w\iff\left[q,w,A\right]\vdash^{*}\left[p,\varepsilon,\varepsilon\right]{% endequation %}

כאן צד שמאל הוא גזירה בדקדוק, וצד ימין הוא חישוב של האוטומט. שימו לב לאופן הפשוט שבו כל הסיבוך של "הפעם הראשונה שבה מה שמתחת ל-{% equation %}A{% endequation %} נחשף" מבוטא כאן - אני פשוט מתאר את החישוב כאילו הוא מתחיל ממחסנית שבה אין כלום מתחת ל-{% equation %}A{% endequation %}, ובצעד האחרון המחסנית מתרוקנת. לא ייתכן שהמחסנית גם לפני הצעד האחרון כי אז האוטומט היה נתקע. לא קשה להוכיח שאם {% equation %}\left[q,w,A\right]\vdash^{*}\left[p,\varepsilon,\varepsilon\right]{% endequation %} אז גם {% equation %}\left[q,w,A\beta\right]\vdash^{*}\left[p,\varepsilon,\beta\right]{% endequation %} לכל {% equation %}\beta{% endequation %} אפשרי, כך שאנחנו לא מגבילים את הכלליות בכך שאנחנו מדברים רק על מה שקורה שהמחסנית ריקה. מעכשיו, לצורך פשטות, אני אדבר על סדרת מעברים כזו פשוט בתור "מעברים שמרוקנים את {% equation %}A{% endequation %}" למרות שפורמלית זה לא ממש נכון (כי {% equation %}A{% endequation %} יכול לעוף במעבר הראשון אבל מה שמתחתיו לא ייחשף מייד, או ש-{% equation %}A{% endequation %} יישאר למשך הרבה זמן, וכו').

אם אני אצליח לבנות דקדוק שאלו משתניו, זה מסיים כמעט מייד את ההוכחה - שימו לב כמה צד ימין של השקילות דומה להגדרת הקבלה באמצעות ריקון מחסנית. כדי לסיים את הבניה אני אוסיף לדקדוק משתנה התחלתי {% equation %}S{% endequation %} (חייב להיות משתנה התחלתי וטרם ציינתי כזה) ולכל מצב {% equation %}p\in Q{% endequation %} אוסיף את הגזירה {% equation %}S\to\left(q_{0},\bot,p\right){% endequation %}, וסיימנו: {% equation %}w\in L\left(M\right){% endequation %} אם ורק אם קיים {% equation %}p\in Q{% endequation %} כך ש-{% equation %}\left[q_{0},w,\bot\right]\vdash^{*}\left[p,\varepsilon,\varepsilon\right]{% endequation %}, כלומר אם ורק אם קיים {% equation %}p\in Q{% endequation %} כך ש-{% equation %}\left(q_{0},\bot,p\right)\Rightarrow^{*}w{% endequation %}, כלומר אם ורק אם {% equation %}S\Rightarrow^{*}w{% endequation %} (למה? זה דורש טיפה נימוק), כלומר אם ורק אם {% equation %}w\in L\left(G\right){% endequation %}.

אז נשאר רק להבין איך לבנות את הדקדוק כך שהשקילות תתקיים. מה זה אומר "לבנות את הדקדוק"? את המשתנים כבר ציינתי - אלו כל השלשות {% equation %}\left(q,A,p\right){% endequation %}; רק נשאר להציג את כללי הגזירה שלהם. פורמלית, הדקדוק שלי הוא {% equation %}G=\left(\left\{ S\right\} \cup Q\times\Gamma\times Q,\Sigma,S,P\right){% endequation %} ורק נותר לי לתאר את {% equation %}P{% endequation %}.

הבניה תתבסס, מן הסתם, על המעברים של האוטומט. אפשר לחלק את המעברים לשני סוגים: כאלו ש<strong>מפשטים</strong> לנו את הסיטואציה, וכאלו ש<strong>מסבכים</strong> אותה (או לכל הפחות משאירים אותה ללא שינוי), וזאת בהתאם לשאלה מה קורה למחסנית. צעד שמסיר את התו מהמחסנית ולא דוחף כלום במקומו עושה לנו את החיים פשוטים יותר; צעד שלא מקטין את המחסנית מסבך אותנו.

המקרה הראשון הוא מעבר מהצורה {% equation %}\left(p,\varepsilon\right)\in\delta\left(q,\sigma,A\right){% endequation %}. שימו לב מה מעבר כזה עושה: הוא מעביר אותנו מ-{% equation %}q{% endequation %} אל {% equation %}p{% endequation %} תוך שהוא מרוקן את {% equation %}A{% endequation %} מהמחסנית - בדיוק מה שהמשתנה {% equation %}\left(q,A,p\right){% endequation %} בא לתאר. מכיוון שהמעבר הזה משתמש ב-{% equation %}\sigma{% endequation %} לצורך כך (ייתכן ש-{% equation %}\sigma{% endequation %} היא המילה הריקה), אז אנחנו מקבלים את הגזירה {% equation %}\left(q,A,p\right)\to\sigma{% endequation %}.

ועכשיו לסיטואציה המסובכת - מעבר מהצורה {% equation %}\left(p,B_{1}B_{2}\dots B_{n}\right)\in\delta\left(q,\sigma,A\right){% endequation %}. כאן {% equation %}A{% endequation %} הוחלף על ידי {% equation %}B_{1}\dots B_{n}{% endequation %} ולכן כדי להשיג את האפקט של ריקון {% equation %}A{% endequation %} מהמחסנית, אנחנו צריכים לרוקן את {% equation %}B_{1},\dots,B_{n}{% endequation %}. זה מזמין את הגזירה הבאה:

{% equation %}\left(q,A,q_{n+1}\right)\to\sigma\left(q_{1},B_{1},q_{2}\right)\left(q_{2},B_{2},q_{3}\right)\cdots\left(q_{n},B_{n},q_{n+1}\right){% endequation %}

שמתארת את הסיפור הבא: קודם כל עברנו מ-{% equation %}q{% endequation %} אל {% equation %}q_{1}{% endequation %} תוך קריאת {% equation %}\sigma{% endequation %} והחלפת {% equation %}A{% endequation %} ב-{% equation %}B_{1}\cdots B_{n}{% endequation %}; אחר כך נעבור מ-{% equation %}q_{1}{% endequation %} אל {% equation %}q_{2}{% endequation %} ונרוקן את {% equation %}B_{1}{% endequation %} תוך כדי; מ-{% equation %}q_{2}{% endequation %} נעבור אל {% equation %}q_{3}{% endequation %} תוך ריקון {% equation %}B_{2}{% endequation %} וכן הלאה, עד אשר נעבור מ-{% equation %}q_{n}{% endequation %} אל {% equation %}q_{n+1}{% endequation %} תוך ריקון {% equation %}B_{n}{% endequation %}.

הכל טוב ויפה חוץ מדבר אחד - מי לכל הרוחות הם המצבים {% equation %}q_{1},q_{2},\dots,q_{n+1}{% endequation %}? מאיפה הם באו? כל מי שהיו לי במעבר המקורי באוטומט היו {% equation %}q,p{% endequation %}, ולאן {% equation %}p{% endequation %} נעלם באמת?

אז בבירור {% equation %}q_{1}=p{% endequation %}, אבל זה עדיין לא מסביר מיהם המצבים {% equation %}q_{2},\dots,q_{n+1}{% endequation %}. התשובה היא ש<strong>אני לא יודע</strong>. המטרה של הגזירה של {% equation %}\left(q,A,q_{n+1}\right){% endequation %} היא לתאר את <strong>כל</strong> הריצות האפשריות שבהן יסירו את {% equation %}B_{1}\cdots B_{n}{% endequation %} מהמחסנית, ואני לא יודע מה מצבי הביניים בהן יהיו. אז מה שאני עושה הוא <strong>לכסות את כל האפשרויות</strong>. כלומר, אני הולך להוסיף את הגזירה

{% equation %}\left(q,A,q_{n+1}\right)\to\sigma\left(q_{1},B_{1},q_{2}\right)\left(q_{2},B_{2},q_{3}\right)\cdots\left(q_{n},B_{n},q_{n+1}\right){% endequation %}

עבור <strong>כל </strong>בחירת ערכים אפשרית ל-{% equation %}q_{2},\dots,q_{n+1}{% endequation %}. ומה קורה אם, למשל, אין דרך להגיע מ-{% equation %}q_{1}{% endequation %} אל {% equation %}q_{2}{% endequation %} תוך הסרת {% equation %}B_{1}{% endequation %} עבור בחירה מסויימת של {% equation %}q_{2}{% endequation %}? אין בעיה. אז הגזירה הזו "תיתקע" כי המשתנה {% equation %}\left(q_{1},B_{1},q_{2}\right){% endequation %} לא יצליח לגזור מילה טרמינלית. לא נורא - אני לא חייב שכל נסיון גזירה יצליח.

קרוב לודאי שחלק מכם תוהים עכשיו למה טרחתי לפצל את כללי הגזירה לשניים, כשבעצם יש לי רק כלל גזירה אחד בשני המקרים - ה"פשוט" וה"מסובך": הכלל {% equation %}\left(q,A,q_{n+1}\right)\to\sigma\left(q_{1},B_{1},q_{2}\right)\left(q_{2},B_{2},q_{3}\right)\cdots\left(q_{n},B_{n},q_{n+1}\right){% endequation %} עם האילוץ ש-{% equation %}p=q_{1}{% endequation %}. המקרה ה"פשוט" מתקבל כאשר {% equation %}n=0{% endequation %}. ובכן, אפשר לעשות את זה כך, אבל לדעתי זה פשוט מבלבל יותר ואני לא רואה בזה טעם. כדאי להזכיר למי ששכח או לא יודע שהרעיון במתמטיקה הוא להיות ברור; לא להיות מינימליסטי. מינימליזם הוא טוב אם הוא מפשט עניינים, אבל אני לא חושב שהוא מטרה בפני עצמה.

בואו נעבור עכשיו להוכחה חצי פורמלית לכך שהבניה עובדת. אני חושב שכאן מאוד מועיל לראות הוכחה כזו כי למרות שאני מקווה שכבר יש לנו אינטואיציה לא רעה לגבי מה הבניה הזו ומאיפה היא הגיעה, עדיין חסר משהו כדי להשתכנע שזה אכן עובד. כזכור, כל מה שנשאר לי להוכיח הוא את הטענה {% equation %}\left(q,A,p\right)\Rightarrow^{*}w\iff\left[q,w,A\right]\vdash^{*}\left[p,\varepsilon,\varepsilon\right]{% endequation %}. זו טענת אם-ורק-אם כך שאני צריך להוכיח שני כיוונים. נטפל בכל אחד מהם בנפרד.

נתחיל מכך שנתון {% equation %}\left(q,A,p\right)\Rightarrow^{*}w{% endequation %} ונוכיח ש-{% equation %}\left[q,w,A\right]\vdash^{*}\left[p,\varepsilon,\varepsilon\right]{% endequation %}. כלומר, אם המשתנה {% equation %}\left(q,A,p\right){% endequation %} גוזר מילה כלשהי, אז המילה הזו מעבירה את האוטומט מ-{% equation %}q{% endequation %} אל {% equation %}p{% endequation %} תוך סילוק {% equation %}A{% endequation %} מהמחסנית. נוכיח את זה באינדוקציה, וזו הזדמנות טובה לשאול את עצמנו - אינדוקציה על מה? כלל האצבע הוא זה - נסתכל על האובייקט שאת קיומו אנחנו מניחים וממנו אנחנו רוצים להסיק דברים, ונבצע אינדוקציה על מאפיין כלשהו שלו שהולך ונעשה מורכב יותר. כאן האובייקט הנתון הוא <strong>הגזירה</strong> של {% equation %}w{% endequation %} מתוך המשתנה; הפרמטר יהיה אורך הגזירה. הבסיס הוא גזירה בת צעד אחד, וזה קל - בגזירה בת צעד אחד שגוזרת מילה טרמינלית ממשתנה, צעד הגזירה חייב להיות כזה שלא יוצר משתנים אלא רק טרמינלים, כלומר הוא חייב להיות גזירה מהצורה ה"פשוטה", {% equation %}\left(q,A,p\right)\to\sigma{% endequation %}. מכאן אנחנו לומדים שני דברים: ש-{% equation %}w=\sigma{% endequation %}, וש-{% equation %}\left(p,\varepsilon\right)\in\delta\left(q,\sigma,A\right){% endequation %}. מסקנה: {% equation %}\left[q,w,A\right]=\left[q,\sigma,A\right]\vdash\left[p,\varepsilon,\varepsilon\right]{% endequation %}.

נעבור אל צעד האינדוקציה. כאן אנחנו מניחים שהטענה נכונה לכל גזירה מאורך קטן מ-{% equation %}k{% endequation %} (עבור {% equation %}k\ge2{% endequation %}) ומוכיחים עבור {% equation %}\left(q,A,p\right)\Rightarrow^{k}w{% endequation %}. התעלול הוא לרוב לפרק את הגזירה לצעד ראשון או אחרון, ו"כל היתר" שעליהם אפשר להפעיל את הנחת האינדוקציה. כאן יהיה לנו נוח לפרק לפי הצעד הראשון, שחייב להיות גזירה מהצורה ה"מסובכת", כי אחרת נקבל מילה טרמינלית אחרי הצעד הראשון ולכן לא ייתכן שהגזירה היא בת שני צעדים או יותר.

כלומר, מתקיים {% equation %}\left(q,A,p\right)\Rightarrow\sigma\left(p,B_{1},q_{2}\right)\left(q_{2},B_{2},q_{3}\right)\cdots\left(q_{n},B_{n},q_{n+1}\right)\Rightarrow^{*}w{% endequation %} וזה נובע מכך שבאוטומט קיים המעבר {% equation %}\left(p,B_{1}B_{2}\dots B_{n}\right)\in\delta\left(q,\sigma,A\right){% endequation %}. בגזירה שמתוארת כאן, כל אחד מהמשתנים מתישהו נגזר לגמרי למילה טרמינלית כלשהי; בואו נסמן אותן באופן הבא: {% equation %}\left(q_{i},B_{i},q_{i+1}\right)\Rightarrow^{*}w_{i}{% endequation %}. המסקנה היא ש-{% equation %}w=\sigma w_{1}\cdots w_{n}{% endequation %}, ושניתן להפעיל את הנחת האינדוקציה על כל גזירה מהצורה {% equation %}\left(q_{i},B_{i},q_{i+1}\right)\Rightarrow^{*}w_{i}{% endequation %} (כי הן בנות פחות מ-{% equation %}k{% endequation %} צעדים) ולקבל {% equation %}\left[q_{i},w_{i},B\right]\vdash^{*}\left[q_{i+1},\varepsilon,\varepsilon\right]{% endequation %}.

עכשיו נחבר את כל אלו כדי לקבל הוכחה לכך ש-{% equation %}\left[q,w,A\right]\vdash^{*}\left[p,\varepsilon,\varepsilon\right]{% endequation %}:

{% equation %}\left[q,w,A\right]=\left[q,\sigma w_{1}\cdots w_{n},A\right]\vdash\left[p,w_{1}\cdots w_{n},B_{1}\dots B_{n}\right]\vdash^{*}{% endequation %}

{% equation %}\vdash^{*}\left[q_{2},w_{2}\cdots w_{n},B_{2}\cdots B_{n}\right]\vdash^{*}\left[q_{n},w_{n},B_{n}\right]\vdash^{*}\left[q_{n+1},\varepsilon,\varepsilon\right]{% endequation %}

וקיבלנו את המבוקש. זה מסיים את הכיוון הזה של ההוכחה.

הכיוון השני דומה באופיו אבל אני אנפנף בו קצת יותר בידיים. הפעם נתון לי {% equation %}\left[q,w,A\right]\vdash^{*}\left[p,\varepsilon,\varepsilon\right]{% endequation %} ואני רוצה להוכיח ש-{% equation %}\left(q,A,p\right)\Rightarrow^{*}w{% endequation %} - ושוב, אעשה זאת באינדוקציה, הפעם על אורך החישוב באוטומט. אם החישוב הוא בן צעד בודד, אז הצעד הזה חייב להיות מהצורה {% equation %}\left(p,\varepsilon\right)\in\delta\left(q,\sigma,A\right){% endequation %} (אחרת לא היה אפשר לרוקן את {% equation %}A{% endequation %} מהמחסנית) ו-{% equation %}w=\sigma{% endequation %}. מסקנה: בדקדוק שבנינו קיים הכלל {% equation %}\left(q,A,p\right)\rightarrow\sigma{% endequation %} וקיבלנו ש-{% equation %}\left(q,A,p\right)\Rightarrow^{*}\sigma=w{% endequation %}. יופי, זה היה קל.

עכשיו לצעד: נניח שהטענה נכונה לכל חישוב מאורך קטן מ-{% equation %}k{% endequation %}. ונוכיח עבור חישוב באורך {% equation %}k{% endequation %} כאשר {% equation %}k\ge2{% endequation %}. אם {% equation %}\left[q,w,A\right]\vdash^{k}\left[p,\varepsilon,\varepsilon\right]{% endequation %} אז נוח לפרק על פי הצעד הראשון, שחייב להיות כזה ש<strong>לא</strong> מרוקן את המחסנית (אחרת לא היה אחריו עוד צעד). כלומר, הצעד הראשון משתמש במעבר מהצורה {% equation %}\left(q_{1},B_{1}B_{2}\dots B_{n}\right)\in\delta\left(q,\sigma,A\right){% endequation %}, ולכן החישוב מתחיל כך: {% equation %}\left[q,w,A\right]\vdash\left[q_{1},w^{\prime},B_{1}\cdots B_{n}\right]{% endequation %}, כאשר {% equation %}w=\sigma w^{\prime}{% endequation %}. כאן מגיע נפנוף הידיים.

מה שאני אומר הוא זה: אני יודע שמהקונפיגורציה {% equation %}\left[q_{1},w^{\prime},B_{1}\cdots B_{n}\right]{% endequation %} החישוב נמשך עד שהוא מסתיים בקונפיגורציה {% equation %}\left[p,\varepsilon,\varepsilon\right]{% endequation %}. בפרט, המחסנית ריקה בסוף וסיימנו לקרוא את כל {% equation %}w^{\prime}{% endequation %}. מכיוון שהמחסנית ריקה, היה חייב להיות רגע שבו {% equation %}B_{2}{% endequation %} נחשף לראשונה (כלומר, בניסוח הלא פורמלי שהשתמשתי בו עד כה, רגע שבו "{% equation %}B_{1}{% endequation %} מוסר מהמחסנית"). וכמו כן חייב להיות רגע שבו {% equation %}B_{3}{% endequation %} נחשף, וכן הלאה, עד הרגע האחרון, שבו המחסנית מתרוקנת.

אם כן, אני אפרק את {% equation %}w^{\prime}{% endequation %} בהתאם לרגעים הללו: {% equation %}w_{1}{% endequation %} הוא כל מה שהאוטומט קרא עד לרגע שבו {% equation %}B_{2}{% endequation %} נחשף, ו-{% equation %}w_{2}{% endequation %} הוא כל מה שהאוטומט קרא עד לרגע שבו {% equation %}B_{3}{% endequation %} נחשף, וכן הלאה. כמו כן, אני אקרא בשם {% equation %}q_{2}{% endequation %} למצב שאליו מגיעים בדיוק כש-{% equation %}B_{2}{% endequation %} נחשף, וכן הלאה. שימו לב לכך ש-{% equation %}w^{\prime}=w_{1}\cdots w_{n}{% endequation %}.

אם כן, הסימונים שנתתי מתארים את הסיטואציה הבאה: {% equation %}\left[q_{i},w_{i}w_{i+1}\cdots w_{n},B_{i}B_{i+1}\cdots B_{n}\right]\vdash^{*}\left[q_{i+1},w_{i+1}\cdots w_{n},B_{i+1}\cdots B_{n}\right]{% endequation %}. כעת לנפנוף הידיים האחרון: מכיוון שבחישוב הזה אין ל-{% equation %}w_{i+1}\cdots w_{n}{% endequation %} שום השפעה (כי עוד לא הגענו לחלק הזה בקלט) וכמו כן גם ל-{% equation %}B_{i+1}\cdots B_{n}{% endequation %} אין שום השפעה (כי האוטומט לא רואה אותם בשום שלב של החישוב - כאן קריטית לגמרי העובדה שאני מסיים את החלק הזה של החישוב בדיוק כאשר {% equation %}B_{i+1}{% endequation %} נחשף <strong>לראשונה</strong>), הרי שאפשר פשוט להתעלם מהם - כלומר, מתקיים {% equation %}\left[q_{i},w_{i},B_{i}\right]\vdash^{*}\left[q_{i+1},\varepsilon,\varepsilon\right]{% endequation %}. וזה מצויין עבורי, כי על הדבר הזה אפשר להשתמש בהנחת האינדוקציה - הוא מהצורה המתאימה (אני מסיים בקונפיגורציה שבה הקלט שנותר והמחסנית שניהם ריקים) והוא מתאר חישוב באורך קטן מ-{% equation %}k{% endequation %} (כי הוא חלק מחישוב באורך {% equation %}k{% endequation %} בלי הצעד הראשון של אותו חישוב). קיבלנו ש-{% equation %}\left(q_{i},B_{i},q_{i+1}\right)\Rightarrow^{*}w_{i}{% endequation %} לכל {% equation %}1\le i\le n{% endequation %}.

כעת אפשר לסיים על ידי הצגת גזירה של {% equation %}w{% endequation %}:

{% equation %}\left(q,A,p\right)\Rightarrow\sigma\left(q_{1},B_{1},q_{2}\right)\cdots\left(q_{n},B_{n},q_{n+1}\right)\Rightarrow^{*}\sigma w_{1}w_{2}\cdots w_{n}=\sigma w^{\prime}=w{% endequation %}

וזה מסיים את הכיוון השני של ההוכחה, ואת ההוכחה כולה.

לסיכום, עכשיו יש לנו שתי דרכים שונות לתאר בהן שפות חסרות הקשר - או על ידי דקדוק, או על ידי אוטומט. באופן לא מפתיע, אני הולך להמשיך להשתמש בדקדוקים רוב הזמן כי זה יותר נוח, אבל פה ושם יש דברים שאוטומט יותר נוח עבורם וטוב שיש לנו בחירה. בפרט, כשאתם נתקלים בשפה ותוהים בינכם לבין עצמכם אם היא חסרת הקשר או לא (ולמי מאיתנו זה לא קרה?), הרבה פעמים במקום לנסות להמציא דקדוק עבור השפה נוח לחשוב בצורה "אלגוריתמית" על האופן שבו אוטומט מחסנית יקבל אותה.