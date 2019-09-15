---
id: 1329
title: "משפט המטריצה-עץ של קירכהוף"
date: 2011-09-13 20:35:51
layout: post
categories: 
  - אלגברה לינארית
  - תורת הגרפים
tags: 
  - אלגברה לינארית
  - גם טכני זה כיף!
  - הוכחות יפות
  - משפט קירכהוף
  - תורת הגרפים האלגברית
---
אני רוצה לדבר הפעם על מה שלטעמי הוא משפט יפהפה ביותר, גם בשל מה שהוא אומר וגם בשל ההוכחה שלו, שלטעמי מייצגת את כל מה שטוב במתמטיקה - גם דורשת הבנה טכנית לא טריוויאלית, וגם מכילה תובנה עמוקה שמאפשרת לראות מדוע המשפט נכון. העולם מסכים איתי, וההוכחה הזו מככבת בספר "Proofs from THE BOOK"; אני מקווה שכל מי שיתאמץ יצליח להבין אותה וליהנות כמוני ממנה.

המשפט מכונה בשם Matrix-tree theorem, או משפט קירכהוף (קירכהוף לא בדיוק הוכיח אותו אבל במאמר שלו המשפט מופיע באופן מובלע). כדי להגיע ישר לעניין ללא הקדמה ארוכה לא אציג מחדש את מושגי הבסיס שבהם עוסק המשפט; כדי להבין את הניסוח (וההוכחה) של המשפט יהיה צורך להכיר את מושגי הבסיס של גרף, עץ, מטריצה ודטרמיננטה. כולם מושגים פשוטים ומרכזיים במתמטיקה ואני ממליץ לקוראים שטרם שמעו עליהם ללכת ולקרוא ספרים בסיסיים בקומבינטוריקה ובאלגברה לינארית כי הם מפספסים עולמות נפלאים שלמים.

ראשית אציג גרסה של המשפט שעוסקת בגרפים לא מכוונים כי ההוכחה שלו פשוטה מעט יותר; לאחר מכן אסביר כיצד ניתן להוכיח את המשפט גם לגרפים מכוונים (באותה הצורה אבל עם תיקונים קלים). המשפט בא לענות על השאלה הקומבינטורית הבאה: בהינתן גרף סופי {% equation %}G=\left(V,E\right){% endequation %}, כמה עצים פורשים יש לו? כזכור, עץ פורש של {% equation %}G{% endequation %} הוא תת-קבוצה של הקשתות שמהווה עץ (כלומר, כשמורידים מ-{% equation %}G{% endequation %} את כל הקשתות שאינן בתת-הקבוצה נשארים עם גרף קשיר וחסר מעגלים). עובדה אחת שאתם אולי לא זוכרים והיא רלוונטית כאן היא שבגרף עם {% equation %}n=\left|V\right|{% endequation %} צמתים, כל עץ הוא בעל בדיוק {% equation %}n-1{% endequation %} קשתות (נסו להוכיח זאת לעצמכם!)

משפט קירכהוף אומר שבהינתן {% equation %}G{% endequation %} כזה, מספר העצים הפורשים שלו הוא בדיוק הדטרמיננטה של מטריצה פשוטה מסויימת שמוגדרת באמצעות {% equation %}G{% endequation %}. זה נשמע מאוד מאוד מפתיע ממבט ראשון - מה לדטרמיננטים ולספירת עצים פורשים? ובכן, אני מודה שגם אחרי שאני מכיר את הוכחת המשפט ומבין בדיוק למה הוא עובד, זה עדיין מפתיע אותי.

בואו נכניס מטריצות לתמונה. יש כמה וכמה מטריצות שאפשר להתאים לכל גרף {% equation %}G{% endequation %}, ואחת מהן היא <strong>מטריצת הלפלסיאן</strong> {% equation %}L_{G}{% endequation %} (ובקיצור אכתוב סתם {% equation %}L{% endequation %}). ההגדרה של {% equation %}L{% endequation %} אולי תיראה קצת מוזרה במבט ראשון אבל היא שימושית; למשל, עבור משפט קירכהוף.

ראשית, מכיוון שמטריצות מאונדקסות בדרך כלל עם מספרים טבעיים, הבה ונאנדקס גם את הגרף עם מספרים כאלו: {% equation %}V=\left\{ v_{1},\dots,v_{n}\right\} {% endequation %} ו-{% equation %}E=\left\{ e_{1},\dots,e_{m}\right\} {% endequation %}. בדרך כלל כשאתייחס לצומת זה יהיה עם אינדקס {% equation %}i{% endequation %} או {% equation %}j{% endequation %}, ולקשת עם אינדקס {% equation %}k{% endequation %}.

כעת אנו מוכנים להגדיר את {% equation %}L{% endequation %}: ראשית, {% equation %}L_{ii}=d\left(v_{i}\right){% endequation %}, כלומר הכניסה ה-{% equation %}i{% endequation %} על האלכסון של {% equation %}L{% endequation %} היא פשוט הדרגה של {% equation %}v_{i}{% endequation %} - מספר הקשתות שמחוברות ל-{% equation %}v_{i}{% endequation %}. כעת, לכל {% equation %}i\ne j{% endequation %} נגדיר את {% equation %}L_{ij}{% endequation %} להיות מינוס מספר הקשתות בין {% equation %}v_{i}{% endequation %}ל-{% equation %}v_{j}{% endequation %} (בדרך כלל יש רק קשת אחת בין כל שני צמתים בגרף, אבל כאן אנחנו מרשים יותר; כמובן שככל שיש יותר קשתות יהיו יותר עצים פורשים). אם נסמן את המספר הזה בסימון שהמצאתי כרגע, {% equation %}d\left(v_{i},v_{j}\right){% endequation %} ונסכים ש-{% equation %}d\left(v_{i},v_{i}\right){% endequation %} הוא פשוט דרגת {% equation %}v_{i}{% endequation %} (במקום מספר הקשתות מ-{% equation %}v_{i}{% endequation %} לעצמו), הרי שאפשר לכתוב את הלפלסיאן כך: {% equation %}L_{ij}=d\left(v_{i},v_{j}\right){% endequation %}.

בשלב הזה צריך להראות דוגמה כדי להבין מה קורה פה. אני אנקוט בגישה שונה - <strong>אתם</strong> תציירו לעצמכם דוגמה, כי זה הרבה יותר אפקטיבי מלקרוא דוגמה שמישהו אחר כתב (וכי אני עצלן), ואני אשב בצד ואחכה שתסיימו.

הגדרת הלפלסיאן עבור גרפים מכוונים כמעט זהה, בשני שינויים קלים: ראשית, {% equation %}L_{ii}{% endequation %} הוא <strong>דרגת הכניסה</strong> של {% equation %}v_{i}{% endequation %} - מספר הקשתות שנכנסות אליו - ולא הדרגה הכוללת; שנית, {% equation %}L_{ij}{% endequation %} הוא מינוס מספר הקשתות מ-{% equation %}v_{i}{% endequation %} <strong>אל</strong> {% equation %}v_{j}{% endequation %} (כלומר, קשתות מ-{% equation %}v_{j}{% endequation %} אל {% equation %}v_{i}{% endequation %} לא נספרות ב-{% equation %}L_{ij}{% endequation %}, אם כי הן כן ייספרו ב-{% equation %}L_{ji}{% endequation %}). לא קשה לראות שההגדרה הזו מכלילה את ההגדרה לגרפים לא מכוונים אם נוקטים בתעלול הרגיל של לייצג גרף לא מכוון על ידי גרף מכוון שבו לכל זוג צמתים שיש ביניהם קשת בגרף הלא מכוון, היא מוחלפת בקשת לכל אחד משני הכיוונים בגרף המכוון.

כעת, יהא {% equation %}r{% endequation %} אינדקס של צומת כלשהו בגרף, ונסמן ב-{% equation %}L^{\left(r\right)}{% endequation %} את <strong>מטריצת המינור</strong> ה-{% equation %}r{% endequation %}-ית של {% equation %}L{% endequation %} - המטריצה שמתקבלת מ-{% equation %}L{% endequation %} על ידי מחיקת השורה והעמודה ה-{% equation %}r{% endequation %}-יות. אז הנה משפט קירכהוף, בגרסה שנכונה הן לגרפים מכוונים והן לגרפים לא מכוונים:

מספר העצים הפורשים של הגרף {% equation %}G{% endequation %} שהשורש שלהם הוא {% equation %}v_{r}{% endequation %} הוא {% equation %}\det L^{\left(r\right)}{% endequation %}.

(בגרף לא מכוון אין ממש משמעות ל"שורש" ולכן כדי למצוא את מספר העצים הפורשים אפשר לבחור {% equation %}r{% endequation %} שרירותי; בגרף מכוון שורש הוא הצומת היחיד בעץ שקיים מסלול ממנו אל שאר הצמתים בגרף).

שימו לב שעניין המינור הכרחי: לא קשה לראות ש-{% equation %}\det L=0{% endequation %} תמיד כי סכום כל עמודה במטריצה הוא 0 ולכן שורות המטריצה תלויות לינארית. כמובן ש-{% equation %}L{% endequation %} מעניינת גם לכשעצמה - למשל, יש חשיבות גדולה לערך העצמי הבא החיובי הקטן ביותר שלה; אבל לא אכנס לכל זה כרגע.

איך מוכיחים את המשפט? אפשר לנסות לחשב ישירות את הדטרמיננטה על פי ההגדרה ולהבין מה הולך שם. זו הוכחה לגיטימית ולא מעט ספרים נוקטים בה. אני מעדיף להשתמש בגישה אחרת ששולפת עוד כמה שפנים מהכובע ובסוף מאפשרת להבין בדיוק מה קורה פה - גישה שמשתמשת בנוסחת קושי-בינה.

את קושי-בינה לא רואים בדרך כלל בקורס בסיסי באלגברה לינארית וקצת חבל. יש לה גם הוכחה קומבינטורית יפהפיה משל עצמה (גם היא ב-Proofs from THE BOOK) שלא אציג כרגע. בבסיסה, הנוסחה היא הכללה של נוסחה בסיסית שכן רואים באלגברה לינארית: אם {% equation %}A,B{% endequation %} הן מטריצות ריבועיות, אז {% equation %}\det\left(A\cdot B\right)=\det A\cdot\det B{% endequation %}.

העניין הוא בכך שמטריצות ריבועיות עשויות להתקבל גם כמכפלה של מטריצות לא ריבועיות: אם {% equation %}A{% endequation %} היא מטריצה {% equation %}n\times m{% endequation %} ו-{% equation %}B{% endequation %} היא מטריצה {% equation %}m\times n{% endequation %} אז מכפלתם {% equation %}AB{% endequation %} היא מטריצה {% equation %}n\times n{% endequation %}, ולכן אפשר לדבר על הדטרמיננטה שלה. מצד שני, {% equation %}A,B{% endequation %} אינן ריבועיות ולכן אין משמעות לדטרמינטטה שלהן. האם בכל זאת אפשר לעשות משהו?

אם {% equation %}m&lt;n{% endequation %} אין על מה לדבר, אבל רק כי אז מובן מאליו ש-{% equation %}\det AB=0{% endequation %}. למה מובן מאליו? ובכן, זה תרגיל טוב באלגברה לינארית: אם {% equation %}m&lt;n{% endequation %} אז דרגת {% equation %}A,B{% endequation %} היא לכל היותר {% equation %}m{% endequation %} כל אחד; ולכן דרגת המכפלה {% equation %}AB{% endequation %} גם היא לכל היותר {% equation %}m{% endequation %}, ולכן {% equation %}AB{% endequation %} היא מטריצה מדרגה לא מלאה ובהכרח הדטרמיננטה שלה היא 0.

מצד שני, אם {% equation %}m&gt;n{% endequation %}, נוסחת קושי בינה נכנסת לפעולה. במילים מה שהולך כאן הוא הדבר הבא: {% equation %}A{% endequation %} היא מטריצה מלבנית, אבל היא מכילה הרבה תת-מטריצות ריבועיות {% equation %}n\times n{% endequation %}, שמתקבלות מבחירת תת-קבוצה של {% equation %}n{% endequation %} מתוך {% equation %}m{% endequation %} העמודות שלה. באותו האופן גם {% equation %}B{% endequation %} מכילה הרבה תת-מטריצות ריבועיות {% equation %}n\times n{% endequation %} שמתקבלות מבחירת תת-קבוצה של {% equation %}n{% endequation %} מתוך {% equation %}m{% endequation %} השורות שלה. אם נסמן ב-{% equation %}\sigma{% endequation %} בחירה מסויימת של {% equation %}n{% endequation %} מתוך {% equation %}m{% endequation %} אינדקסים, אז נוסחת קושי-בינה היא פשוט {% equation %}\det\left(AB\right)=\sum_{\sigma}\left(\det A_{\sigma}\cdot\det B_{\sigma}\right){% endequation %}. כלומר: לכל בחירה אפשרית של {% equation %}n{% endequation %} מתוך {% equation %}m{% endequation %} אינדקסים {% equation %}\sigma{% endequation %} ניקח מתוך {% equation %}A{% endequation %} ו-{% equation %}B{% endequation %} את תת המטריצות המתאימות (שימו לב שזו <strong>אותה בחירת אינדקסים</strong> לשתי המטריצות! זה מה שחשוב פה), נחשב את מכפלת הדטרמיננטות שלהן, ונסכום את הכל (אם {% equation %}m&lt;n{% endequation %} אז אפשר להסכים על כך שהסכום ריק ולכן שווה 0, ובכך לקבל נוסחה שתקפה לכל מקרה אפשרי).

איך נוסחת קושי-בינה מסייעת לנו כאן? ובכן, את הלפלסיאן קל למדי לכתוב כמכפלה של מטריצות. בואו נדבר לבינתיים על המקרה של גרף לא מכוון שהוא פשוט קצת יותר, ונגדיר מטריצה {% equation %}A{% endequation %} - "מטריצת החילה" (Incidence matrix) של הגרף. זו תהיה מטריצה {% equation %}n\times m{% endequation %} שבה כל שורה מייצגת צומת בגרף וכל עמודה מייצגת קשת בגרף, כך שלכל קשת {% equation %}e_{k}=\left(v_{i},v_{j}\right){% endequation %} עם {% equation %}i&lt;j{% endequation %} נקבע ש-{% equation %}A_{ik}=1,A_{jk}=-1{% endequation %} וכל כניסה אחרת במטריצה היא 0. במילים אחרות, כל עמודה במטריצה הזו מכילה בדיוק 1 בודד ו-{% equation %}-1{% endequation %} בודד, בשני הצמתים שמתאימים לקשת של אותה עמודה.

כעת זה תרגיל נחמד לבדוק שאכן {% equation %}L=A\cdot A^{T}{% endequation %} (כאן {% equation %}A^{T}{% endequation %} מייצג את השחלוף של {% equation %}A{% endequation %}: {% equation %}A_{ij}^{T}=A_{ji}{% endequation %}). ומהו {% equation %}L^{\left(r\right)}{% endequation %}? לא קשה לראות שהוא {% equation %}NN^{T}{% endequation %} כאשר {% equation %}N{% endequation %} מתקבלת מ-{% equation %}A{% endequation %} על ידי מחיקת השורה ה-{% equation %}r{% endequation %}. שימו לב שאנחנו לא מוחקים מ-{% equation %}A{% endequation %} עמודות; הקשתות שהיו מחוברות ל-{% equation %}v_{r}{% endequation %} עדיין מיוצגות ב-{% equation %}N{% endequation %}, אבל באופן "חלקי" - העמודה שלהן מכילה רק 1 או רק {% equation %}-1{% endequation %}. זו אולי הנקודה הקריטית ביותר בהמשך ההוכחה.

עכשיו, על פי קושי-בינה, {% equation %}\det\left(L^{\left(r\right)}\right)=\sum_{\sigma}\det N_{\sigma}\det N_{\sigma}^{T}=\sum_{\sigma}\det\left(N_{\sigma}\right)^{2}{% endequation %}. הצטמצמנו להבנה של מהו {% equation %}\det\left(N_{\sigma}\right){% endequation %} לכל בחירה מתאימה של עמודות. שימו לב של-{% equation %}N{% endequation %} יש {% equation %}n-1{% endequation %} שורות (כי בגרף המקורי היו {% equation %}n{% endequation %} צמתים והסרנו את השורה של הצומת {% equation %}v_{r}{% endequation %} מהמטריצה {% equation %}A{% endequation %} כדי לקבל את {% equation %}N{% endequation %}), ולכן כל {% equation %}\sigma{% endequation %} היא בחירה של {% equation %}n-1{% endequation %} עמודות, כלומר של {% equation %}n-1{% endequation %} קשתות מהגרף המקורי. והנה לב ההוכחה, התובנה המרכזית בה, מה שהופך את הכל לברור לדעתי: אותה בחירה {% equation %}\sigma{% endequation %} של {% equation %}n-1{% endequation %} עמודות היא <strong>בדיקה שלנו האם מועמד כלשהו לתפקיד עץ פורש הוא אכן עץ פורש</strong>. הדטרמיננטה {% equation %}\det N_{\sigma}{% endequation %} תהיה בדיוק אבן הבוחן: אם {% equation %}\sigma{% endequation %} אכן מהווה בחירה של {% equation %}n-1{% endequation %} קשתות שיוצרות עץ פורש, נקבל ש-{% equation %}\det N_{\sigma}=\pm1{% endequation %}; ואחרת נקבל {% equation %}\det N_{\sigma}=0{% endequation %}. זה בבירור מסיים את ההוכחה שכן אז נקבל ש-{% equation %}\sum_{\sigma}\det\left(N_{\sigma}\right)^{2}{% endequation %} הוא בדיוק מספר ה-{% equation %}\sigma{% endequation %}-ות שעבורן קיבלנו עץ פורש, כלומר מספר העצים הפורשים של הגרף.

אתם עוד איתי? אם כן, הבנתם את ההוכחה; נותר לגהץ את הפרטים.

נתחיל במקרה שבו {% equation %}\sigma{% endequation %} לא מגדירה עץ פורש בגרף {% equation %}G{% endequation %}. אנחנו רוצים להראות ש-{% equation %}\det N_{\sigma}=0{% endequation %} במקרה הזה, ונעשה זאת על ידי כך שנוכיח שבמטריצה {% equation %}N_{\sigma}{% endequation %} יש קבוצה של שורות שסכומן אפס. תוצאה בסיסית על עצים היא שאם גרף לא מכוון עם {% equation %}n{% endequation %} צמתים ו-{% equation %}n-1{% endequation %} קשתות הוא גם קשיר, אז הוא עץ; לכן אם {% equation %}\sigma{% endequation %} אינה משרה עץ בהכרח יש שני רכיבי קשירות. {% equation %}v_{r}{% endequation %} נמצא באחד מהם; בואו נסתכל דווקא על השני - וליתר דיוק, על השורות במטריצה {% equation %}N_{\sigma}{% endequation %} שמתאימות לצמתים של אותו רכיב קשירות שני. אני טוען שסכום כל השורות הללו הוא 0. מדוע? ובכן, נעבור עמודה עמודה: כל עמודה מתאימה לקשת שמחברת שני צמתים. אם שניהם אינם ברכיב הקשירות ממילא, אז בשורות שמתאימות לרכיב הקשירות כל הכניסות בעמודה הזו יהיו 0. אם שניהם ברכיב הקשירות, אז תהיה שורה שבה יופיע 1, ושורה שבה יופיע {% equation %}-1{% endequation %}, ובשאר השורות 0 - ושוב, הסכום הוא 0. ואם אחד מהצמתים ברכיב הקשירות והשני לא? ובכן, זה בלתי אפשרי כי זה נוגד את ההגדרה של רכיב קשירות: אם צומת נמצא ברכיב קשירות מסויים, כך גם כל שכניו.

הטיעון הטכני ביותר יהיה ההוכחה ש-{% equation %}\det N_{\sigma}=\pm1{% endequation %} כאשר {% equation %}\sigma{% endequation %} כן מתאימה לעץ פורש, אבל אחר כך סיימנו את ההוכחה כולה. הרעיון הוא שבמקרה הזה, אפשר לסדר מחדש את שורות ועמודות {% equation %}N_{\sigma}{% endequation %} כך שתתקבל מטריצה משולשית תחתונה (מטריצה שבה כל הכניסות מעל לאלכסון הראשי הן 0), ואת הדטרמיננטה של מטריצה משולשית קל לחשב - זו בסך הכל מכפלת האיברים שעל האלכסון. מכיוון שסידור מחדש של שורות או עמודות משנה רק את הסימן של הדטרמיננטה, זה יסיים את ההוכחה. את המטריצה המסודרת-מחדש אסמן ב-{% equation %}M{% endequation %}.

אמרנו ש-{% equation %}\sigma{% endequation %} מהווה עץ. מה שנעשה הוא להתחיל לפרק את העץ לגורמים. ראשית, בואו נזכור ש<strong>עלה</strong> בעץ הוא צומת מדרגה 1, כלומר שמחובר בדיוק לצומת אחר אחד. עוד משפט חשוב על עצים הוא שבעץ יש לפחות שני עלים; לא אוכיח אותו כרגע.

הבה ונסמן ב-{% equation %}u_{1}{% endequation %} עלה שכזה<strong> </strong>שהוא <strong>שונה </strong>מ-<strong>{% equation %}v_{r}{% endequation %} </strong>(תמיד יש כזה; אפילו אם {% equation %}v_{r}{% endequation %} הוא עלה, יש עוד עלה שאפשר לבחור) וב-{% equation %}e_{1}{% endequation %} את הקשת בעץ שמחוברת אליו. השורה הראשונה במטריצה-המסודרת-מחדש שלנו תהיה זו של {% equation %}u_{1}{% endequation %}, והעמודה הראשונה תהיה זו של {% equation %}e_{1}{% endequation %}. מכיוון ש-{% equation %}u_{1}{% endequation %} מחובר <strong>רק</strong> ל-{% equation %}e_{1}{% endequation %} בעץ, הכניסה {% equation %}M_{11}{% endequation %} תהיה שווה ל-1 או ל-{% equation %}-1{% endequation %}(לא משנה לנו איזה מהם), וכמו כן {% equation %}M_{1j}=0{% endequation %} לכל {% equation %}j&gt;1{% endequation %} (ובכלל לא משנה איך אני הולך לסדר את יתר העמודות), שכן כל העמודות הללו מתאימות לקשתות ש-{% equation %}u_{1}{% endequation %} לא מחובר אליהן.

כעת נסיר את {% equation %}u_{1}{% endequation %} מהעץ שלנו (ויחד איתו את {% equation %}e_{1}{% endequation %}), ושוב נקבל עץ, ולכן שוב יש בו צומת מדרגה 1 שאינו {% equation %}v_{r}{% endequation %}. זה יהיה {% equation %}u_{2}{% endequation %} והקשת שמתאימה לו תהיה {% equation %}e_{2}{% endequation %}. זה אומר ש-{% equation %}M_{22}{% endequation %} הוא שוה {% equation %}\pm1{% endequation %}; ואנו יודעים בודאות שעבור הקשתות שטרם טיפלנו בהן, {% equation %}u_{2}{% endequation %} אינו מחובר לאף אחת מהן ולכן {% equation %}M_{2j}=0{% endequation %} לכל {% equation %}j&gt;2{% endequation %} (אולי הוא היה מחובר ל-{% equation %}e_{1}{% endequation %}, אבל זה אומר רק שאולי {% equation %}M_{12}\ne0{% endequation %} וזה לא מפריע לנו כי כניסה זו היא <strong>מתחת</strong> לאלכסון הראשי). העיקרון ברור - נמשיך לבנות כך סדרה {% equation %}u_{1},u_{2},\dots,u_{n-1}{% endequation %} של צמתים ו-{% equation %}e_{1},e_{2},\dots,e_{n-1}{% endequation %} של קשתות. הצומת היחיד שלא נגענו בו הוא {% equation %}v_{r}{% endequation %} עצמו, שהשורה שמתאימה לו בכלל לא מופיעה ב-{% equation %}N{% endequation %} כך שהוא לא רלוונטי לבניה שעשינו. קיבלנו מטריצה משולשת תחתונה שעל האלכסון יש לה רק {% equation %}\pm1{% endequation %} וזה מסיים את ההוכחה.

אני מאוד מקווה שנהניתם מההוכחה הזו כפי שאני נהניתי ממנה.

בואו נעבור עכשיו לדבר על מה צריך להשתנות בהוכחה אם נרצה להוכיח את המשפט לגרפים מכוונים. כבר אמרתי שצריך לשנות את הגדרת מטריצת הלפלסיאן עצמה קצת: {% equation %}L_{ii}{% endequation %} הוא דרגת הכניסה של כל צומת ו-{% equation %}L_{ij}{% endequation %} הוא מינוס מספר הקשתות מ-{% equation %}v_{i}{% endequation %} <strong>אל</strong> {% equation %}v_{j}{% endequation %}. זו לא מטריצה סימטרית ולכן גם לא בהכרח ניתן לכתוב אותה בתור {% equation %}A\cdot A^{T}{% endequation %}; אבל אפשר לעשות משהו טוב כמעט באותה מידה.

הבה ונגדיר שוב מטריצה {% equation %}A{% endequation %} מסדר {% equation %}n\times m{% endequation %} (כלומר - שורה לכל צומת ועמודה לכל קשת, כמקודם) באופן הבא: לכל קשת {% equation %}e_{k}=v_{i}\to v_{j}{% endequation %} (כלומר, מהצומת {% equation %}v_{i}{% endequation %} אל הצומת {% equation %}v_{j}{% endequation %}) יתקיים {% equation %}A_{ik}=1,A_{jk}=-1{% endequation %} ושאר הכניסות יהיו אפס; במילים אחרות, זו בדיוק אותה מטריצה {% equation %}A{% endequation %} כמו קודם רק שעכשיו אנחנו קובעים איזו כניסה תהיה חיובית ואיזו כניסה תהיה שלילית על פי כיוון הקשת {% equation %}e_{k}{% endequation %}.

בנוסף, נגדיר מטריצה {% equation %}B{% endequation %} מסדר {% equation %}n\times m{% endequation %} באופן הבא: לכל קשת {% equation %}e_{k}=v_{i}\to v_{j}{% endequation %} יתקיים {% equation %}B_{ik}=0,B_{jk}=-1{% endequation %} ושאר הכניסות יהיו אפס. כלומר, {% equation %}B{% endequation %} זהה ל-{% equation %}A{% endequation %} פרט לכך שבכל עמודה יש רק {% equation %}-1{% endequation %} עבור הצומת שאליו הקשת נכנסת; לא מופיע 1 עבור הצומת שממנו הקשת יוצאת.

עכשיו לא קשה לראות ש-{% equation %}L=A\cdot B^{T}{% endequation %} וש-{% equation %}L^{\left(r\right)}{% endequation %} הוא {% equation %}N_{A}N_{B}^{T}{% endequation %} כאשר {% equation %}N_{A},N_{B}{% endequation %} מתקבלים מ-{% equation %}A,B{% endequation %} בהתאמה על ידי מחיקת השורה ה-{% equation %}r{% endequation %}. אז קושי-בינה מניבה פה {% equation %}\det\left(L^{\left(r\right)}\right)=\sum_{\sigma}\det\left(N_{A\sigma}\right)\det\left(N_{B\sigma}\right){% endequation %}. עכשיו צריך להבין מה קורה פה.

היינו רוצים לומר שאם {% equation %}\sigma{% endequation %} לא מגדיר עץ, אז נקבל ש-{% equation %}\det\left(N_{A\sigma}\right)=0{% endequation %} בדיוק כמו קודם ואז גם המכפלה תתאפס. לרוע המזל, "{% equation %}\sigma{% endequation %} לא מגדיר עץ" הוא מקרה הרבה יותר מסובך כאשר הגרף שלנו מכוון, כי הקריטריון של "גרף עם {% equation %}n-1{% endequation %} קשתות שהוא קשיר הוא עץ" פשוט לא נכון. בעץ מכוון, צריך שיהיה צומת (השורש) שקיים מסלול ממנו לכל הצמתים האחרים, ומספיקה קשת אחת בכיוון הלא נכון כדי לקלקל את זה. לכן בואו נתחיל קודם כל דווקא מדיבור על המקרה שבו {% equation %}\sigma{% endequation %} כן מגדיר עץ. מה נשתנה הפעם?

ובכן, הפעם צריכים להיות קצת יותר זהירים בגלל ש-{% equation %}\det\left(N_{A\sigma}\right)\det\left(N_{B\sigma}\right){% endequation %} הוא לא ריבוע. מה שאנחנו רוצים לטעון הוא שמתקיים {% equation %}\det\left(N_{A\sigma}\right)=\det\left(N_{B\sigma}\right){% endequation %} וששניהם שווים או 1 או {% equation %}-1{% endequation %}. אפשר להשתמש בשיטת הסידור-מחדש של מטריצה כמו קודם; רק צריך להיות זהירים ולסדר את {% equation %}N_{A\sigma}{% endequation %} ואת {% equation %}N_{B\sigma}{% endequation %} באותו האופן בדיוק כדי שהשינוי בסימן, אם היה כזה, יהיה זהה אצל שניהם.

אחרי הסידור מחדש של המטריצה, מה שמתקבל מ-{% equation %}N_{A\sigma}{% endequation %} ומ-{% equation %}N_{B\sigma}{% endequation %} היא כמקודם מטריצה משולשית תחתונה, אבל מה נמצא על האלכסון? כאן האופן שבו ביצענו את הסדר הופך להיות קריטי: להזכירכם, בשיטה שלנו בשלב ה-{% equation %}i{% endequation %} קבענו את השורה ה-{% equation %}i{% endequation %} להיות צומת {% equation %}u_{i}{% endequation %} שבשלב הזה היה עלה, ואת העמודה להיות קשת {% equation %}e_{i}{% endequation %} שהיא הקשת ש<strong>נכנסת</strong> אל {% equation %}u_{i}{% endequation %}. כלומר, הן על פי ההגדרה של {% equation %}A{% endequation %} והן על פי ההגדרה של {% equation %}B{% endequation %}, הכניסה המתאימה תהיה {% equation %}-1{% endequation %}. זה מבטיח שהדטרמיננטה תהיה מכפלה של {% equation %}-1{% endequation %}-ים ושלא ישתרבב פנימה איזה 0 שיאפס את כולה (מה שהיה עלול לקרות עם {% equation %}B{% endequation %}, שבו יש אפסים שלא היו בהוכחה עבור גרפים לא מכוונים).

עכשיו נחזור למקרה שבו {% equation %}\sigma{% endequation %} הוא לא עץ. מי שיושיע אותנו כאן הוא שאנחנו משתמשים גם ב-{% equation %}N_{A\sigma}{% endequation %} וגם ב-{% equation %}N_{B\sigma}{% endequation %}: הדטרמיננטה של אחד מהם תתאפס, ולא משנה מה. התעלול פשוט: אם {% equation %}\sigma{% endequation %} הוא כזה שאפילו גרף התשתית של העץ שלנו (מה שמקבלים כשמוחקים את כיווני הקשתות) איננו עץ אז {% equation %}\det\left(N_{A\sigma}\right)=0{% endequation %} מאותו שיקול כמו במקרה הלא מכוון (סכום שורות שהוא אפס, מה שמובטח על ידי ה-1 וה-{% equation %}-1{% endequation %} שיש בכל עמודה שם - וזה משהו שאין ב-{% equation %}B{% endequation %}), ואילו אם גרף התשתית הוא כן עץ, אז נסדר מחדש את {% equation %}N_{B\sigma}{% endequation %} על פי אותה שיטה שבה השתמשנו עד כה במקרים שבהם {% equation %}\sigma{% endequation %} הגדיר עץ. נקבל מטריצה משולשית תחתונה כמו תמיד, רק שהפעם אחד מהאיברים על האלכסון יהיה 0. מדוע? כי אם {% equation %}\sigma{% endequation %} איננו עץ למרות שגרף התשתית הוא כן עץ, זה אומר שיש קשת אחת שמכוונת בכיוון "הלא נכון", ואז הכניסה על האלכסון שמתאימה לקשת הזו ולצומת שמחוברת אליה תהיה 0 (כי הקשת <strong>יוצאת</strong> מהצומת במקום להיכנס אליו).

אם כן, המקרה המכוון הוא מעט יותר מסובך מהמקרה הלא מכוון אבל גם בו יש תובנות יפות לגבי <strong>למה</strong> זה עובד - ושוב, אני מקווה שנהניתם.